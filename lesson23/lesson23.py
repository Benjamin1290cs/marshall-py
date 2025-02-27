# Lesson 23

loop = True
counter = 0
total_sum = 0

while loop:
    user_input = input("Enter the mark or \"Exit\" to exit: ")
    if user_input.lower().capitalize() == "Exit":
        loop = False
        break
    else:
        mark = int(user_input)
        if 0 <= mark <= 100:
            total_sum += mark
            counter += 1
        else:
            print("Invalid input.")

average = total_sum / counter

print(average)




