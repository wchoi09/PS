class Solution(object):
    def twoSum(Self, nums, target):
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if n + nums[j] == target:
                    return [i, j]
