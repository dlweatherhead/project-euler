def find_sum_of_even_values(sequence):
    total = 0
    for x in sequence:
        if x % 2 == 0:
            total += x
    return total


def next_fibonacci_number(current, previous):
    return current + previous


def generate_fibonacci_sequence(upper_limit):
    sequence = [0, 1]
    previous = 0
    current = 1
    while True:
        new_value = next_fibonacci_number(current, previous)
        if new_value > upper_limit:
            return sequence
        previous = current
        current = new_value
        sequence.append(current)


seq = generate_fibonacci_sequence(100)
print(seq)
even_sum = find_sum_of_even_values(seq)
print(even_sum)

seq = generate_fibonacci_sequence(4000000)
print(seq)
even_sum = find_sum_of_even_values(seq)
print(even_sum)
