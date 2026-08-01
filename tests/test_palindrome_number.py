import unittest

from python.easy.palindrome_number import Solution


class PalindromeNumberTests(unittest.TestCase):
    def test_returns_true_for_a_palindrome(self):
        self.assertTrue(Solution().isPalindrome(121))

    def test_returns_false_for_a_non_palindrome(self):
        self.assertFalse(Solution().isPalindrome(10))

    def test_returns_false_for_a_negative_number(self):
        self.assertFalse(Solution().isPalindrome(-121))

    def test_returns_true_for_zero(self):
        self.assertTrue(Solution().isPalindrome(0))
