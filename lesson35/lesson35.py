# Lesson 35

def dupe_remover(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

test = ["a","b","c","c","b","c","a", "a", "d"]
print(f"test list: {test}")
print(f"duplicates removed: {dupe_remover(test)}")