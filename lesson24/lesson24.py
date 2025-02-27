# Lesson 24
loop = True
max_name = ""

while loop:
    user_input = input("Enter a name or enter \'X\' to exit: ")
    if user_input.lower().capitalize() == "X":
        loop = False
        break
    else:
        if len(user_input) > len(max_name):
            max_name = user_input

if max_name == "":
    print("Insufficient data.")
else:
    print(max_name)
