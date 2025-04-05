# 22. Remove given words from a string
def remove_words():
    text = input("Enter a sentence: ")
    word = input("Enter word to remove: ")
    print("Updated text:", text.replace(word, ''))
remove_words()
