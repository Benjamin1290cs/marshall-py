# Lesson 39

def gcd(num1, num2):
    for divider in range(min(num1, num2), 0, -1):
        if num1 % divider == 0 and num2 % divider == 0:
            return divider
    return 1

print(gcd(1080,27)) 
