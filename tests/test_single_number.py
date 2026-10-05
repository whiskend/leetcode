import unittest

from python.easy.single_number import Solution


class SingleNumberTests(unittest.TestCase):
    def test_finds_the_unpaired_number(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), 1)

    def test_handles_separated_duplicate_pairs(self):
        self.assertEqual(Solution().singleNumber([4, 1, 2, 1, 2]), 4)

    def test_handles_a_negative_unpaired_number(self):
        self.assertEqual(Solution().singleNumber([-2, 7, -3, -2, 7]), -3)

    def test_handles_zero_as_the_unpaired_number(self):
        self.assertEqual(Solution().singleNumber([-1, 0, -1]), 0)

    def test_handles_a_single_element(self):
        self.assertEqual(Solution().singleNumber([5]), 5)
