# Lesson 41

def score_finder(text):
    score = 0
    for character in text:
        character = character.upper()
        if character in "AEIOULNRST":
            score += 1
        elif character in "DG":
            score += 2
        elif character in "BCMP":
            score += 3
        elif character in "FHVWY":
            score += 4
        elif character in "K":
            score += 5
        elif character in "JX":
            score += 8
        elif character in "QZ":
            score += 10
    return score

def highest_score(a_list):
    max_score = 0
    best_word = ""
    for word in a_list:
        current_score = score_finder(word)
        if current_score > max_score:
            max_score = current_score
            best_word = word
    return best_word, max_score

text = [
    "hello", 
    "great",
    "poop",
]

best_word, max_score = highest_score(text)
print(f"The word with the highest score is '{best_word}' with a score of {max_score}.")

