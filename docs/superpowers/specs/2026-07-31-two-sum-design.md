# Two Sum Design

## Goal

Create the first easy LeetCode solution in Python: return the indices of two numbers whose sum equals a target.

## Approach

Use a one-pass hash map. While reading each number, look up the number needed to reach `target`; if it has already appeared, return its index and the current index. Otherwise, store the current number and index.

This makes one pass through the input and uses extra space for previously seen values.

## Files

- `python/easy/two_sum.py`: a `Solution.twoSum(nums, target)` method compatible with LeetCode.
- `tests/test_two_sum.py`: tests for a standard example, duplicate values, and a valid pair that appears later in the list.
- `README.md`: repository overview and how to run the tests.

## Error Handling

The LeetCode problem guarantees exactly one solution, so the method returns an empty list only if it receives input outside that guarantee.

## Validation

Run the test suite with Python's built-in `unittest` runner. The tests verify returned index pairs, including the duplicate-number case where a value cannot be reused at the same index.
