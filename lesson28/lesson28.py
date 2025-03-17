# Lesson 28

def is_palindrome(text):
    return text == text[::-1]

def is_palindrome2(text):
    if not text:
        return True
    elif len(text) < 4:
        return text[0] == text[-1]
    else:
        midpoint = len(text) // 2
        for i in range(0, midpoint):
            left = text[i]
            right = text[-1*i -1]
            if right != left:
                return False
        return True

text = input("Enter a text: ")

if is_palindrome2(text):
    print(f"{text} is a palindrome.")
else: 
    print(f"{text} is not a palindrome.")
