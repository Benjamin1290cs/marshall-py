# Lesson 44

def c_frequency(text):
    result = {}
    clean_word = sorted(text.lower())

    for character in clean_word:
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1
    return result

print(c_frequency("hello"))

