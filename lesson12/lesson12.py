# Lesson 12

# input
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

# processing and output
angle_sum = angle1 + angle2 + angle3

if angle_sum != 180:
    print("Invalid angles.")
else:
    if angle1 == angle2 == angle3:
        print("Equilateral triangle.")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isoceles triangle.")
    else:
        print("Scalene triangle.")
