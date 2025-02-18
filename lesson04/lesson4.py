# Lesson 4

# import statement
from math import ceil

# input
lineOne = input("Enter section 1: ")
lengthOne = len(lineOne)
lineTwo = input("Enter section 2: ")
lengthTwo = len(lineTwo)
lineThree = input("Enter section 3: ")
lengthThree = len(lineThree)

# processing
totalSum = (lengthOne, lengthTwo, lengthThree)
cans = sum(totalSum)

boxes = ceil(cans /12)
leftovers = 12*boxes - cans

totalCost = 14.95 * boxes

# output
print(f"We need {boxes} boxes.")
print(f"There will be {leftovers} leftovers.")
print(f"It will cost ${totalCost}.")