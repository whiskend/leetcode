class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        votes = 0

        for number in nums:
            if votes == 0:
                candidate = number
            votes += 1 if number == candidate else -1

        return candidate
