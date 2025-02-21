# Lesson 7
# import statement
import random

# input 
difficulty = int(input("Enter DC value: "))

# processing & output
player_roll = random.randrange(1 , 21)

print(f"The player has rolled {player_roll} on their D20")

if player_roll >= difficulty:
    print(f"The player was succesful as {player_roll} is >= than {difficulty}.")
else:
    print(f"The player was unsucessful as {player_roll} is < than {difficulty}.")