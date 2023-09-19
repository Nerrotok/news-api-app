import requests
import send_email as se
import config

topic = config.topic

api_key = config.api_key
url = f"https://newsapi.org/v2/everything?q={topic}" \
      "&from=2023-07-07&sortBy=publishedAt&apiKey=" \
      f"{api_key}"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = "Subject: Today's news" \
       + "\n" + body
body = body.encode("utf-8")
se.send_email(body)
