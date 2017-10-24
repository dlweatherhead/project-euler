# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
from palindrome import is_palindrome

if __name__ == '__main__':
    largest = 0
    for i in range(0, 999+1):
        for j in range(0, 999+1):
            n = i * j
            if n > largest:
                if is_palindrome(str(n)):
                    largest = n
    print(largest)
