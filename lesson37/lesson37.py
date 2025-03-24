# Lesson 37

def string_comp(text):
    if not text:  
        return ""
    
    ctr = 1
    result = ""
    
    for character in range(1, len(text)):
        if text[character] == text[character - 1]:
            ctr += 1
        else:
            result += f"{text[character - 1]}{ctr}"
            ctr = 1
            
    result += f"{text[-1]}{ctr}" 
    return result

print(string_comp("aabcccccaaa"))
