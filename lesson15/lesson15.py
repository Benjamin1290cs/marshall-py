# Lesson 15

condition_variable = True
password = "poop"

while condition_variable:
    user_input = input("Guess the password: ")

    if user_input == "poop":
        print("Correct guess!")
        condition_variable = False
    else:
        print("Incorrect guess!")

print("\n")

user_input = input("Search for a fruit:")

fruits = ["Apple", "Banana", "Kiwi", "Strawberry"]
found = False

for fruit_name in fruits:
    if fruit_name == user_input:
        print(f"{user_input} is found!")
        found = True

if not found: 
    print(f"{user_input} is not found...")