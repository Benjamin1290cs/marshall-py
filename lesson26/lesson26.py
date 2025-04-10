# Lesson 26
def is_divisible(num1, num2):
    return num1 % num2 == 0

def factor_count(num):
    counter = 0
    for divider in range(1, num+1):
        if is_divisible(num, divider):
            counter += 1
    return counter

upper_limit = int(input("Enter N: "))
for num in range(1,upper_limit+1):
    print(f"{num} has {factor_count(num)} factors")