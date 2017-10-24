# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math


def divisible_for_range(value, range_list):
    for i in range_list:
        if value % i != 0:
            return False
    return True


def problem_solution(r):
    upper_limit = int(math.pow(r[-1], len(r)))
    for x in range(r[-1], upper_limit):
        if divisible_for_range(x, r):
            return x


if __name__ == '__main__':
    print(problem_solution(range(1, 21)))
