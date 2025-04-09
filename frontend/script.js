document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector("button");
  const resultDiv = document.getElementById("result");

  button.addEventListener("click", async function () {
    // Get user input
    let siteUrl = document.getElementById("siteUrl").value.trim();
    if (!siteUrl) {
      resultDiv.innerHTML = "<p class='error'>Please enter a valid URL.</p>";
      resultDiv.classList.remove("hidden");
      return;
    }

    // Ensure URL has "http://" or "https://"
    if (!siteUrl.startsWith("http://") && !siteUrl.startsWith("https://")) {
      siteUrl = "https://" + siteUrl;
    }

    // API Gateway URL
    const apiUrl =
      "https://149z9efc5j.execute-api.ap-south-1.amazonaws.com/check?url=" +
      encodeURIComponent(siteUrl);

    try {
      // Fetch API Response
      const response = await fetch(apiUrl);
      const data = await response.json();

      // ✅ Handle invalid URL error response
      if (data.error) {
        resultDiv.innerHTML = `<p class='error'>Invalid URL entered. Please check and try again.</p>`;
        resultDiv.classList.remove("hidden");
        return;
      }

      // ✅ Display valid site data
      resultDiv.innerHTML = `
                <h3>Website Status</h3>
                <p><strong>Site Checked:</strong> ${data.site_url}</p>
                <p><strong>Response Time:</strong> ${data.response_time} ms</p>
                <p><strong>Site Status:</strong> <span class="${
                  data.status === "UP" ? "status-up" : "status-down"
                }">${data.status}</span></p>
                <p><strong>Last Downtime:</strong> ${data.last_downtime}</p>
            `;
      resultDiv.classList.remove("hidden");
    } catch (error) {
      console.error("Error fetching data:", error);
      resultDiv.innerHTML =
        "<p class='error'>Error fetching website status. Please try again.</p>";
      resultDiv.classList.remove("hidden");
    }
  });
});
