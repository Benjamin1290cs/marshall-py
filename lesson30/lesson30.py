# Lesson 30

def create_line(num):
    result = ""
    for i in range(1, num+1):
        if i % 2 == 0:
            result += "0"
        else:
            result += "1"
    
    return result

def output_pattern(num):
    for i in range(1, num+1):
        print(create_line(i))

num = int(input("Enter a num: "))
output_pattern(num)

