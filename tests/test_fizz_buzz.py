import unittest

from python.easy.fizz_buzz import Solution


class FizzBuzzTests(unittest.TestCase):
    def test_returns_numbers_without_matching_multiples(self):
        self.assertEqual(Solution().fizzBuzz(2), ["1", "2"])

    def test_returns_fizz_for_a_multiple_of_three(self):
        self.assertEqual(Solution().fizzBuzz(3), ["1", "2", "Fizz"])

    def test_returns_buzz_for_a_multiple_of_five(self):
        self.assertEqual(
            Solution().fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"]
        )

    def test_returns_fizz_buzz_for_a_multiple_of_fifteen(self):
        self.assertEqual(Solution().fizzBuzz(15)[-1], "FizzBuzz")
