import unittest

from python.easy.contains_duplicate import Solution


class ContainsDuplicateTests(unittest.TestCase):
    def test_detects_a_duplicate(self):
        self.assertTrue(Solution().containsDuplicate([1, 2, 3, 1]))

    def test_returns_false_for_distinct_numbers(self):
        self.assertFalse(Solution().containsDuplicate([1, 2, 3, 4]))

    def test_handles_a_single_element(self):
        self.assertFalse(Solution().containsDuplicate([7]))

    def test_detects_repeated_zero(self):
        self.assertTrue(Solution().containsDuplicate([0, 0]))

    def test_detects_a_negative_duplicate(self):
        self.assertTrue(Solution().containsDuplicate([-1, 2, -1]))

    def test_does_not_modify_the_input(self):
        nums = [3, 1, 2, 3]
        self.assertTrue(Solution().containsDuplicate(nums))
        self.assertEqual(nums, [3, 1, 2, 3])
