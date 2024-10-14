import re
from collections import Counter
from dotenv import load_dotenv
import os
from file_management_system import setup_default_directory_structure
from pathlib import Path

load_dotenv()

def convert_list(string):
    ly = list(string.split(" "))
    return ly

def generate_common_words(base_path):
    file_path = base_path / "words" / "common_words.txt"
    with open(file_path, "r") as common:
        words = common.read()
        common_words = list(words.split("\n"))
    return common_words

def clean_article_content(base_path):
    file_path = base_path / "Articles" / "Guardian_articles"
    all_words = []
    if file_path.exists():
        for file in os.listdir(file_path):
            full_file_path = file_path / file
            try:
                with open(full_file_path, "r", encoding="utf-8") as raw_text:
                    article_content = raw_text.read()
                cleaned_content = re.sub(r"[^a-zA-Z\s]", "", article_content.lower())
                words = [word for word in cleaned_content.split() if len(word) > 2]
                print("Cleaned content:", " ".join(words))
                print("\n")
                all_words.extend(words)
            
            except FileNotFoundError:
                print(f"file not found")
                return None
    return all_words

def filter_out_known_words(base_path, common_words, clean_content):
    file_path = base_path / "words" / "word_bank.txt"
    new_words = []
    with open(file_path, "r") as bank:
        known_words = bank.read().split("\n")
    for new_word in clean_content:
        if new_word not in common_words:
            if new_word not in known_words:
                new_words.append(new_word)

    ten_most_common_words = Counter(new_words).most_common(10)
    print(ten_most_common_words)
    return ten_most_common_words

def store_words_in_word_bank(base_path, most_common_words):
    file_path = base_path / "words" / "word_bank.txt"
    with open(file_path, "a") as word_bank:
        res_list = [x[0] for x in most_common_words]
        for word in res_list:
            is_sure = input(f"Do you know the word '{word}' already? Y / N? ").lower().strip() == "y"
            if is_sure == True:
                word_bank.write(str(word) + "\n")
            else:
                print("New word found")
                continue

def main():
    base_path = setup_default_directory_structure()
    common_words = generate_common_words(base_path)
    clean_content = clean_article_content(base_path)
    most_common_words = filter_out_known_words(base_path, common_words, clean_content)
    store_words_in_word_bank(base_path, most_common_words)

if __name__ == "__main__":
    main()