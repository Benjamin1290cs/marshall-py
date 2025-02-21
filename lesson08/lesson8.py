# Lesson 8

# input
win_counter = 0 
for i in range(6):
    current_result = input(f"Enter the game {i+1} result:")
    
    if current_result == "W":
        win_counter += 1 

# processing and output
if win_counter >= 5:
    print("Player is placed in Group 1.")
elif win_counter > 2:
    print("Player is placed in Group 2.")
elif win_counter > 0:
    print("Player is placed in Group 3.")
else:
    print("Eliminated.")
