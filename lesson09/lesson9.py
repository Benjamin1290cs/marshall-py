# Lesson 9
# import statement
from random import choice

invalid = ''

while not invalid:
    player = input("Enter your choice of (rock, paper, or scissors): ")
    if player in (["rock", "paper", "scissors"]):
        invalid = "valid"
    else:
        print("Invalid option. Try again.")

cpu = choice(["rock", "paper", "scissors"])
print (f"The CPU has chosen {cpu}.")

if player == cpu:
    print("Tie.")
else:
    if "rock" in player:
        if "scissors" in cpu:
            print("Player wins.")
        else:
            print("CPU wins.")
    if "scissors" in player:
        if "rock" in cpu:
            print("CPU wins.")
        else:
            print("Player wins.")
    else:
        if "paper" in player:
            if "rock" in cpu:
                print("Player wins.")
            else: 
                print("CPU wins.")