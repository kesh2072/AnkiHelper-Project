from bs4 import BeautifulSoup
import re
import requests

def get_HTML_document(url):
    response = requests.get(url)
    return response.text

def get_url(culture_list):
    #folder_path = "C:\\Users\\kesh2\\ArticleScout\\Urls\\Guardian_urls.txt"
    with open("C:\\Users\\kesh2\\ArticleScout\\Urls\\Guardian_urls.txt", "a", encoding="utf-8") as guardian:
        for value in culture_list:
            for link in value_soup.find_all("a", attrs={"href": re.compile(value + "/2024")}):
                if filter_url(link.get("href")):
                    guardian.write("\nhttps://www.theguardian.com" + link.get("href"))

def filter_url(url: str) -> bool:
    if url.endswith("#comments"):
        return False
    if url.startswith("https://"):
        return False
    return True

url_culture = "https://www.theguardian.com/culture"
html_culture = get_HTML_document(url_culture)
value_soup = BeautifulSoup(html_culture, "html.parser")
culture_list = ["music", "books", "film", "artanddesign"]
get_url(culture_list)
