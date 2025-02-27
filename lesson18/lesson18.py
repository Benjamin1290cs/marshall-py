# Lesson 18

# input 
num = int(input("Enter a number: "))

# processing
for divider in range(1, num+1):
    if num % divider == 0:
        print(f"{divider} is a factor of {num}.")