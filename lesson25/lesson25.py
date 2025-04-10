# Lesson 25

num = int(input("Enter a number: "))
num_copy = num 

largest = 0

while num % 2 == 0:
    num //= 2
    largest = max(largest,2)

if num != 1:
    factor = 3
    while num != 1:
        if num % factor == 0:
            largest = max(largest, factor)
            num //= factor 
        else:
            factor += 2

print(largest)