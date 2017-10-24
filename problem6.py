# The sum of the squares of the first ten natural numbers is,
#
#               12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025 Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import unittest


def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def square_of_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total*total


def get_diff_of_square_sum_and_sum_squares(n):
    return square_of_sum(n) - sum_of_squares(n)


# class TestProblem6(unittest.TestCase):
#     def test_sum_of_squares_true(self):
#         self.assertEqual(sum_of_squares(10), 385)
#
#     def test_square_of_sum_true(self):
#         self.assertEqual(square_of_sum(10), 3025)
#
#     def test_get_diff_of_square_sum_and_sum_squares(self):
#         self.assertEqual(get_diff_of_square_sum_and_sum_squares(10), 2640)


if __name__ == '__main__':
    print(get_diff_of_square_sum_and_sum_squares(100))
