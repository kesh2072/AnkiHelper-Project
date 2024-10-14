import re
import os
from pathlib import Path

def setup_default_directory_structure():
    home_directory = Path.home()

    base_path = home_directory / "ArticleScout"
    articles_dir = base_path / "Articles"
    guardian_articles_dir = articles_dir / "Guardian_articles"
    words_dir = base_path / "words"

    urls_dir = base_path / "Urls"
    guardian_urls_file = urls_dir / "Guardian_urls.txt"
    dw_urls_file = urls_dir / "DW_urls.txt"
    word_bank = words_dir / "word_bank.txt"

    guardian_articles_dir.mkdir(parents=True, exist_ok=True)
    urls_dir.mkdir(parents=True, exist_ok=True)
    #word_bank.mkdir(parents=True, exist_ok=True)

    guardian_urls_file.touch(exist_ok=True)
    dw_urls_file.touch(exist_ok=True)
    #word_bank.touch(exist_ok=True)

    return base_path


def article_title(urls: list[str]) -> list[str]:
    title_names = []
    for url in urls:
        result = str(url).rsplit("/", 1)[-1]
        clean_title = re.sub("-", " ", result).title()
        title_names.append(clean_title)
    return title_names

def text_file_creation(base_path: Path, urls: list[str]):
    folder_path = base_path / "Articles" / "Guardian_articles"

    title_names = article_title(urls)

    for name in title_names:
            file_path = folder_path / f"{name}.txt"
            with open(file_path, "a", encoding="utf-8") as txt:
                txt.write("testing123\n")

if __name__ == "__main__":
    base_path = setup_default_directory_structure()
    urls = ["http://example.com/article-one", "http://example.com/article-two"]
    text_file_creation(base_path, urls)