# Lesson 10

# input
number = input("Enter the last 4 digits of the number: ")

# processing and output
if number[0] == "8" or number[1] == "9":
    if number[1] == number[2]:
        if number[3] == "8" or "9":
            print("ignore")
        else: 
            print("answer")
    else:
        print("answer")
else:
    print("answer")