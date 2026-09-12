import unittest

from python.easy.valid_parentheses import Solution


class ValidParenthesesTests(unittest.TestCase):
    def test_accepts_matching_brackets(self):
        self.assertTrue(Solution().isValid("()[]{}"))

    def test_rejects_mismatched_brackets(self):
        self.assertFalse(Solution().isValid("(]"))

    def test_rejects_wrong_nesting(self):
        self.assertFalse(Solution().isValid("([)]"))

    def test_rejects_unclosed_brackets(self):
        self.assertFalse(Solution().isValid("("))
