# Lesson 43

def dupe_remover(a_list):
    result_list = []

    for value in a_list:
        if value not in result_list:
            result_list.append(value)
    return result_list

def dupe_remover2(a_list):
    return list(set(a_list))

def unique_letters(a_list):
    result_set = set()

    for word in a_list:
        tmp_set = set(word)
        result_set |= tmp_set
    return result_set

def i_count(a_list):
    if a_list:
        result_set = a_list[0]

        for example_set in a_list[1:]:
            result_set = result_set & example_set
        
        return len(result_set)

test1 = [1, 4, 2, 3, 4, 5, 4, 23, 12]
test2 = ["hello", "goodbye", "world", "mr. park!"]
test3 = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(dupe_remover(test1))
print(dupe_remover2(test1))
print(unique_letters(test2))
print(i_count(test3))

