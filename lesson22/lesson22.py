# Lesson 22

upper_limit = int(input("Enter N to find the Nth Fibonacci number: "))

fib_0 = 0
fib_1 = 1
fib_n = 0

for n in range (2, upper_limit+1):
    fib_n = fib_0 + fib_1
    fib_0 = fib_1
    fib_1 = fib_n

print(f"{fib_n} is {upper_limit}'s Nth Fibonacci number.")