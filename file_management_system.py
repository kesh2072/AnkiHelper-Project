from article_parser import urls
import re
import os

def article_title(urls: list[str]) -> list[str]:
    title_names = []
    for url in urls:
        result = str(url).rsplit("/", 1)[-1]
        clean_title = re.sub("-", " ", result).title()
        title_names.append(clean_title)
        print(title_names)
    return title_names

def text_file_creation():
    folder_path = "C:\\Users\\kesh2\\ArticleScout\\Articles\\Guardian"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    title_names = article_title(urls)

    for name in title_names:
        x = os.path.join(folder_path, name)
        with open(x, "a") as txt:
            txt.write("testing123")

text_file_creation()