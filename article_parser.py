import requests
import json
from bs4 import BeautifulSoup
import csv
import re

with open("C:\\Users\\kesh2\\ArticleScout\\Urls\\Guardian_urls.txt", "r") as guardian:
    raw_urls = (guardian.read())

def convert_list(string):
    ly = string.split("\n")
    return [url.strip() for url in ly if url.strip()]

urls = convert_list(raw_urls)

responses = []

def open_and_write_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        responses.append(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        feed = soup.find_all("p")
        feed2 = str(feed)
        clean_feed = re.sub("<[^>]+>", "", feed2)
        with open("C:\\Users\\kesh2\\ArticleScout\\Articles\\BBC_articles\\bbc_test.txt", "a") as bbc:
            bbc.write(clean_feed)
            bbc.write("\n")
    else:
        print(f"Failed to fetch data from {url}")

try:
    open_and_write_article(urls[1])
except Exception as ex:
    print(f"error whilst running article: {ex}")

