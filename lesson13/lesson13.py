# Lesson 13

# input
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# processing and output

if month < 2:
    print("Before")
elif month > 2: 
    print("After")
else:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
    else:
        print("Special")
