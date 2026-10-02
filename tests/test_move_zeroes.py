import unittest

from python.easy.move_zeroes import Solution


class MoveZeroesTests(unittest.TestCase):
    def test_moves_zeroes_in_place_and_returns_none(self):
        nums = [0, 1, 0, 3, 12]

        result = Solution().moveZeroes(nums)

        self.assertIsNone(result)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_preserves_order_of_negative_and_duplicate_values(self):
        nums = [0, -2, 0, 3, -2, 0]

        Solution().moveZeroes(nums)

        self.assertEqual(nums, [-2, 3, -2, 0, 0, 0])

    def test_handles_all_zeroes(self):
        nums = [0, 0, 0]

        Solution().moveZeroes(nums)

        self.assertEqual(nums, [0, 0, 0])

    def test_preserves_a_list_without_zeroes(self):
        nums = [1, -2, 3]

        Solution().moveZeroes(nums)

        self.assertEqual(nums, [1, -2, 3])

    def test_handles_single_element_lists(self):
        for value in [0, 7]:
            with self.subTest(value=value):
                nums = [value]
                Solution().moveZeroes(nums)
                self.assertEqual(nums, [value])
