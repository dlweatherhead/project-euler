import unittest


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def list_of_primes(n):
    prime_list = []
    for x in range(1, n):
        if is_prime(x):
            prime_list.append(x)
    return prime_list


def list_of_primes_up_to(l):
    prime_list = []
    n = 1
    while n < l:
        if is_prime(n):
            prime_list.append(n)
        n += 1
    return prime_list


def find_the_nth_prime(n):
    x = 1
    count = 0
    while count < n:
        x += 1
        if is_prime(x):
            count += 1
    return x


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


class PrimeTest(unittest.TestCase):
    def test_is_prime_false(self):
        self.assertEqual(is_prime(9), False)

    def test_is_prime_true(self):
        self.assertEqual(is_prime(11), True)

    def test_list_of_primes(self):
        self.assertEqual(list_of_primes(10), [2, 3, 5, 7])

    def test_list_of_primes_false_case(self):
        self.assertNotEqual(list_of_primes(10), [2, 3, 4, 5, 7])

    def test_list_of_primes_up_to(self):
        self.assertEqual(list_of_primes_up_to(10), [2, 3, 5, 7])

    def test_prime_factors(self):
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])

    def test_find_the_nth_prime(self):
        self.assertEquals(find_the_nth_prime(6), 13)


if __name__ == "__main__":
    unittest.main()
