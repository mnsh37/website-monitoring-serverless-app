from decimal import Decimal
import json
import requests
import time
import boto3
from datetime import datetime

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("WebsiteMonitoring")

def lambda_handler(event, context):
    """AWS Lambda function to check website status and store data in DynamoDB."""
    
    # Get website URL from query parameters
    site_url = event.get("queryStringParameters", {}).get("url", "").strip()
    
    if not site_url:
        return {"statusCode": 400, "body": json.dumps({"error": "No URL provided"})}

    # Ensure the URL has "http://" or "https://"
    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        site_url = "https://" + site_url  # Default to HTTPS
    
    try:
        # Measure response time
        start_time = time.time()
        response = requests.get(site_url, timeout=10)
        response_time = Decimal(str(round((time.time() - start_time) * 1000, 2)))  # Convert to Decimal
        
        # Determine site status
        site_status = "UP" if response.status_code == 200 else "DOWN"

        # Get last downtime from DynamoDB (if it was previously DOWN)
        last_downtime = "N/A"
        item = table.get_item(Key={"site_url": site_url})
        if "Item" in item and item["Item"]["status"] == "DOWN":
            last_downtime = item["Item"]["last_downtime"]
        
        # ✅ Only store valid URLs in DynamoDB
        if site_status == "UP":
            table.put_item(
                Item={
                    "site_url": site_url,
                    "response_time": response_time,
                    "status": site_status,
                    "last_downtime": last_downtime
                }
            )

        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "site_url": site_url,
                "response_time": str(response_time),  # Convert Decimal to str for JSON response
                "status": site_status,
                "last_downtime": last_downtime
            })
        }

    except requests.exceptions.RequestException:
        # ❌ Do NOT store invalid/unreachable URLs in DynamoDB
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid URL or site unreachable"
            })
        }
