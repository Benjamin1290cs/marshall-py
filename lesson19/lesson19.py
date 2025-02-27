# Lesson 19

# input 
num = int(input("Enter a number: "))

# processing
counter = 0
for divider in range(1, num+1):
    if num % divider == 0:
        counter += 1

# output
if counter == 2:
    print(f"{num} is a prime number.")     
else: 
    print(f"{num} is a composite number.") 