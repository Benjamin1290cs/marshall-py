# Lesson 36

def factor_finder(num):
    result = []
    for divider in range(1, num+1):
        if num % divider == 0:
            result.append(divider)
    return result

def is_prime(num):
    return len(factor_finder(num)) == 2

print(f"Factors of 13: {factor_finder(13)}")
print(f"Factors of 36: {factor_finder(36)}")
print(f"Is 36 prime?: {is_prime(36)}")
print(f"Is 13 prime?: {is_prime(13)}")
