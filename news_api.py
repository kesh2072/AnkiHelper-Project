import os
import requests

#API_KEY = os.getenv("GNEWS_API_KEY")  # store it in env var
url = "https://gnews.io/api/v4/search"

params = {
    "q": "Russland",   # search keyword
    "lang": "de",               # results language
    "country": "de",            # source country
    "max": 2,                   # number of results (1–10)
    "apikey": "9e7d874adf7d26dbe6028d3d3c21d2a7"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for article in data["articles"]:
        print(article["title"])
        print(article["url"])
        print(article['content'])
        print("---")
else:
    print("Error:", response.status_code, response.text)
