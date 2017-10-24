import unittest


def is_palindrome(n):
    count_max = len(n) // 2
    for x in range(0, count_max):
        if n[x] != n[len(n) - x - 1]:
            return False
    return True


class PalindromeTest(unittest.TestCase):
    def test_is_palindrome_odd_false(self):
        self.assertEqual(is_palindrome('12345'), False)

    def test_is_palindrome_odd_true(self):
        self.assertEqual(is_palindrome('90009'), True)

    def test_is_palindrome_even_false(self):
        self.assertEqual(is_palindrome('6789'), False)

    def test_is_palindrome_even_true(self):
        self.assertEqual(is_palindrome('4554'), True)


if __name__ == "__main__":
    unittest.main()
