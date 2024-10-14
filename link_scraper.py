from bs4 import BeautifulSoup
import re
import requests
from file_management_system import setup_default_directory_structure
from pathlib import Path

#folder_path = "C:\\Users\\kesh2\\ArticleScout\\Urls\\Guardian_urls.txt"

def get_HTML_document(url):
    response = requests.get(url)
    return response.text

def get_url(culture_list, folder_path, soup):
    with open(folder_path, "a", encoding="utf-8") as guardian:
        for value in culture_list:
            for link in soup.find_all("a", attrs={"href": re.compile(value + "/2024")}):
                if filter_url(link.get("href")):
                    full_url = "https://www.theguardian.com" + link.get("href")
                    guardian.write("\n" + full_url)

def filter_url(url: str) -> bool:
    if url.endswith("#comments"):
        return False
    if url.startswith("https://"):
        return False
    return True

def generate_folder_path(url, base_path: Path):
    """Generates the appropriate folder path for URLs based on their source."""
    urls_dir = base_path / "Urls"
    
    if url.startswith("https://www.theguardian"):
        folder_path = urls_dir / "Guardian_urls.txt"
    elif url.startswith("https://www.dw"):
        folder_path = urls_dir / "DW_urls.txt"
    else:
        folder_path = urls_dir / "other_urls.txt"
    
    return folder_path


def main():
    base_path = setup_default_directory_structure()
    url_culture = "https://www.theguardian.com/culture"
    html_culture = get_HTML_document(url_culture)
    
    value_soup = BeautifulSoup(html_culture, "html.parser")
    
    culture_list = ["music", "books", "film", "artanddesign"]

    folder_path = generate_folder_path(url_culture, base_path)
    
    get_url(culture_list, folder_path, value_soup)


if __name__ == "__main__":
    main()