import re
from collections import Counter

def convert_list(string):
    ly = list(string.split(" "))
    return ly

with open("common_words.txt", "r") as common:
    words = common.read()
    common_words = list(words.split("\n"))
    print(common_words)


# with open("names.txt", "r") as names:
#     name = names.read()

with open("bbc_text.txt", "r") as raw_text:
    text = raw_text.read()

text_two = text.replace("'", "")
text_three = re.sub("[\W\d_]+", " ", text_two.lower())



text_four = convert_list(text_three)

#- - - - - - - - - - - - - - - - - - 

new_words = []
capitalised_words = []

with open("word_bank.txt", "r") as bank:
    known_words = bank.read().split("\n")

for new_word in text_four:
    if new_word not in common_words: # Can ask user for their language level before hand, to automatically filter out certain words 
        if new_word not in known_words:
            new_words.append(new_word)
print(new_word)

most_common_words = Counter(new_words).most_common(10)
print(most_common_words)

def store_words_in_word_bank():
    with open("word_bank.txt", "a") as word_bank:
        res_list = [x[0] for x in most_common_words]
        for word in res_list:
            is_sure = input(f"Do you know the word '{word}' already? Y / N? ").lower().strip() == "y"
            if is_sure == True:
                word_bank.write(str(word) + "\n")
            else:
                print("New word found")
                continue

store_words_in_word_bank()

