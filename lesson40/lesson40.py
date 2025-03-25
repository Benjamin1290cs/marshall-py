# Lesson 40

def factor_finder(num):
    result = []
    for divider in range(1,num+1):
        if num % divider == 0:
            result.append(divider)
    return result

def is_prime(num):
    return len(factor_finder(num)) == 2

def prime_list(num):
    primes = [2]
    if num == 2:
        return primes
    else:
        for num in range(3, num, 2):
            if is_prime(num):
                primes.append(num)
        return primes

print(prime_list(100))

