# Lesson 11

# input

points = input("Enter x and y values: ")
points = points.split(" ")
points = list(map(int, points))
x, y = points
print(f"The x-value is {x}.")
print(f"The y-value is {y}.")

if x < 0:
    if y > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")
elif x > 0:
    if y > 0:
        print("Quadrant 1")
    else: 
        print("Quadrant 4")
