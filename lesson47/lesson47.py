# Lesson 47

def r_sum(num):
    if num in {0,1}:
        return num
    else:
        return num + r_sum(num-1)

print(r_sum(10))
    

