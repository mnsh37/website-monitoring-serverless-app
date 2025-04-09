# 🌐 Website Monitoring App (AWS Serverless)

A modern, real-time website monitoring tool built using AWS Serverless technologies. Enter any website URL to instantly check its status, response time, and recent downtime—powered entirely by AWS Lambda, API Gateway, and DynamoDB. The frontend is lightweight, responsive, and hosted on Amazon S3.

---

## 🔗 Live Demo

Check out the live working version here: [Website Monitoring App](http://site-monitoring-frontend.s3-website.ap-south-1.amazonaws.com)  
*(Deployed using Amazon S3 Static Website Hosting)*

---

## 🚀 Features

- ✅ Real-time website status check (UP/DOWN)
- 📉 Response time tracking in milliseconds
- 🧠 Downtime history logging via DynamoDB
- 💡 Invalid URL handling and feedback
- 📱 Responsive, modern UI with glassmorphism
- ☁️ 100% Serverless architecture using AWS

---

## 🧰 Tech Stack

### Frontend
- **HTML5**, **CSS3**, **Vanilla JavaScript**
- Hosted on **Amazon S3** (Static Website Hosting)

### Backend (AWS)
- **AWS Lambda** (Python)
- **API Gateway** (REST API)
- **Amazon DynamoDB** (Data Storage)
- **Amazon EventBridge** (Scheduled Checks)

---

## 🖼️ Architecture

```
Client (S3 Static Website)
        ⬇️
    API Gateway (REST)
        ⬇️
     AWS Lambda (Python)
        ⬇️
  Amazon DynamoDB (Stores URL status, response time, last downtime)
```

![Architecture Diagram](architecture-diagram.png)

---

## 📦 Project Structure

```
website-monitoring-app/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/
│   └── lambda_function.py
├── architecture-diagram.png
└── README.md
```

---

## 👨‍💻 Author

**Manish Kumar**  
Built with ❤️ using AWS Serverless  
[LinkedIn](https://www.linkedin.com/mnshkumr)
