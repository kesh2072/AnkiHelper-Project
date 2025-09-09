#from readability import Readability
import readability
from dotenv import load_dotenv
import os

load_dotenv()

base_path = os.getenv('FILE_PATH')


def convert_list(string):
    ly = string.split("\n")
    return ly

def rank_article_complexity():
    with open(base_path + "articles\\Guardian_articles\\Guardian.txt", "r", encoding="utf-8") as article_content:
        list_of_articles = convert_list(article_content.read())

        for article in list_of_articles:
            print(len(article.split()))
            if len(article.split()) < 100:
                print("too short")
                continue
            else:
                r = readability.Readability(article)
                fk = r.flesch()
                print(fk.score, fk.grade_levels)
                print(article, "\n")

def main():
    rank_article_complexity()

if __name__ == "__main__":
    main()