# Palindrome Number Design

## Goal

Add a Python solution for LeetCode's Palindrome Number problem. It returns whether an integer reads the same forward and backward.

## Approach

Use integer arithmetic instead of converting the number to a string. Negative values return `False`; for non-negative values, reverse the digits and compare the result with the original number.

This uses O(log n) time for a number with `log n` digits and O(1) extra space.

## Files

- `python/easy/palindrome_number.py`: LeetCode-compatible `Solution.isPalindrome(x)` method.
- `tests/test_palindrome_number.py`: tests for a palindrome, a non-palindrome, a negative number, and zero.
- `README.md`: a link to the new easy problem.

## Error Handling

LeetCode supplies integers, so no input conversion or validation is needed. Every supplied integer returns a boolean.

## Validation

Run all tests using `python3 -m unittest discover -s tests -v`.
