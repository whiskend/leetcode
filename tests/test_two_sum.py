import unittest

from python.easy.two_sum import Solution


class TwoSumTests(unittest.TestCase):
    def test_returns_indices_for_a_standard_pair(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_uses_two_distinct_duplicate_values(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])

    def test_finds_a_pair_after_an_unmatched_value(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
