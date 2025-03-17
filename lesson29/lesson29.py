# Lesson 29

def consonant_finder(text):
    text = text.lower()
    counter = 0
    for character in text:
        if character.isalpha() and character not in ["a", "e", "i", "o", "u"]:
            counter += 1

    return counter

text = input("Enter a text: ")
result = consonant_finder(text)
print(f"There is {result} consonants in {text}")