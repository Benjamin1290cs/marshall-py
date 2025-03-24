# Lesson 38

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for num1 in range(999, 99, -1):
        for num2 in range(num1, 99, -1):  
            product = num1 * num2
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(largest_palindrome_product())
