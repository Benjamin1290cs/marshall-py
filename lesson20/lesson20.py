# Lesson 20
total_sum = 0

for num in range(1,10000):
    factor_sum = 0
    for divider in range(1, num):
        if num % divider == 0:
            factor_sum += divider
    if factor_sum == num:
        total_sum += num
        print(f"{num} is a perfect number.")

print(f"The total sum of all perfect numbers under 10,000 is {total_sum}")

