# Lesson 21

# input 
num = int(input("Enter a number: "))

# processing
max_count = 0
result_num = 0

for i in range(1, num+1):
    total_factors = 0
    
    for divider in range(1, num+1):
        if i % divider == 0:
            total_factors += 1
    
    if total_factors > max_count:
        max_count = total_factors
        result_num = i

# output
print(f"{result_num} is the factor of {num} with the most factors.")    

