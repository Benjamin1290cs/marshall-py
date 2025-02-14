# Lesson 3
tiles = input("Enter the number of tiles: ")
#input() always a string
tiles = int(tiles)

# Square root is just exponent of a half
calculation = int((tiles ** 0.5) // 1)

print(f"The maximum side length is: {calculation}")
# #OR
# import math
# calculations = math.sqrt(tiles)
