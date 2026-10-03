import unittest

from python.easy.search_insert_position import Solution


class SearchInsertPositionTests(unittest.TestCase):
    def test_finds_an_existing_target(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 5), 2)

    def test_inserts_between_two_values(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 2), 1)

    def test_inserts_before_the_first_value(self):
        self.assertEqual(Solution().searchInsert([-3, 0, 4], -5), 0)

    def test_inserts_after_the_last_value(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 7), 4)

    def test_handles_a_single_element(self):
        for target, expected in [(4, 0), (5, 0), (6, 1)]:
            with self.subTest(target=target):
                self.assertEqual(Solution().searchInsert([5], target), expected)
