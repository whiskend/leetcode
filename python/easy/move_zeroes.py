class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        next_nonzero = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[next_nonzero], nums[index] = nums[index], nums[next_nonzero]
                next_nonzero += 1
