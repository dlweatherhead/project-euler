def find_sum_of_multiples(value, x, y):
    total = 0
    for num in range(0, value):
        if is_multiple_of(num, x, y):
            total += num
    return total


def is_multiple_of(value, x, y):
    if value % x == 0:
        return True
    elif value % y == 0:
        return True
    return False


print(find_sum_of_multiples(10, 3, 5))
print(find_sum_of_multiples(1000, 3, 5))
