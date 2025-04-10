# Lesson 45

def word_length(a_list):
    result = {}
    for word in a_list:
        result[word] = len(word)
    return result

# return {key : len(key) for key in a_list}

def d_fib(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] = result[i-1] + result[i-2]
        return result



test = ["apple", "blueberry", "orange", "banana"]
print(word_length(test))
print(d_fib(10))