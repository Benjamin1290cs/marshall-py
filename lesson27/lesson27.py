# Lesson 27

def string_cleaner(text):
    cleaned = ""
    for character in text:
        if character.isalpha():
            cleaned += character.lower()
        
    return cleaned

text = input("Enter text: ")
result = string_cleaner(text)

print(result)
