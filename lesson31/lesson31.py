# Lesson 31

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else: 
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
    return True

word1 = input("Enter text 1: ")
word2 = input("Enter text 2: ")

if is_anagram(word1, word2):
    print("True")
else:
    print("False")