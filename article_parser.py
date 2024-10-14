import requests
from bs4 import BeautifulSoup
import re
from dotenv import load_dotenv
import os
from file_management_system import article_title, setup_default_directory_structure

load_dotenv()

base_path = os.getenv('FILE_PATH')

# def get_full_file_path(sub_dir):
#     if not base_path:
#         raise ValueError("Base file path is not set. Please configure the FILE_PATH environment variable.")

#     full_path = os.path.join(base_path, sub_dir)

#     if not os.path.exists(full_path):
#         os.makedirs(full_path)

#     return full_path

# articles_path = get_full_file_path("articles")
# urls_path = get_full_file_path('Urls')


def initialise_list_of_urls(urls_path):
    Guardian_urls = urls_path / "Guardian_urls.txt"
    with open(Guardian_urls, "r") as guardian:
        raw_urls = (guardian.read())
    urls = convert_list(raw_urls)
    return urls

def convert_list(string):
    ly = string.split("\n")
    return [url.strip() for url in ly if url.strip()]


responses = []

def open_and_write_article(url, base_path):
    response = requests.get(url)
    if response.status_code == 200:
        responses.append(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        feed = soup.find_all("p")
        str_feed = str(feed)
        clean_feed = re.sub("<[^>]+>", "", str_feed)

        article_titles = article_title([url])
        article_title_str = article_titles[0]

        articles_dir = base_path / "Articles" / "Guardian_articles"
        article_file_path = articles_dir / f"{article_title_str}.txt"

        with open(article_file_path, "w", encoding="utf-8") as article_file:
            article_file.write(clean_feed)
            article_file.write("\n")
        
        print(f"Article saved: {article_file_path}")
        
    else:
        print(f"Failed to fetch data from {url}")

def main():
    base_path = setup_default_directory_structure()
    
    urls_path = base_path / "Urls"

    urls = initialise_list_of_urls(urls_path)

    for url in urls:
        open_and_write_article(url, base_path)

if __name__ == "__main__":
    main()
