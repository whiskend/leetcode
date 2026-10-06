import unittest

from python.easy.majority_element import Solution


class MajorityElementTests(unittest.TestCase):
    def test_finds_the_majority_element(self):
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)

    def test_finds_a_majority_that_is_not_the_first_element(self):
        self.assertEqual(Solution().majorityElement([1, 2, 3, 2, 2]), 2)

    def test_handles_a_negative_majority(self):
        self.assertEqual(Solution().majorityElement([-1, 2, -1, 3, -1]), -1)

    def test_handles_zero_as_the_majority(self):
        self.assertEqual(Solution().majorityElement([0, 1, 0, 2, 0]), 0)

    def test_handles_a_single_element(self):
        self.assertEqual(Solution().majorityElement([7]), 7)
