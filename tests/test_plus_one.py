import unittest

from python.easy.plus_one import Solution


class PlusOneTests(unittest.TestCase):
    def test_increments_without_a_carry(self):
        self.assertEqual(Solution().plusOne([1, 2, 3]), [1, 2, 4])

    def test_carries_across_trailing_nines(self):
        self.assertEqual(Solution().plusOne([1, 9, 9]), [2, 0, 0])

    def test_adds_a_digit_when_all_digits_are_nine(self):
        self.assertEqual(Solution().plusOne([9, 9]), [1, 0, 0])

    def test_increments_zero(self):
        self.assertEqual(Solution().plusOne([0]), [1])
