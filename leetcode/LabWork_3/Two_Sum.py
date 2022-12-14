"""
1. Two Sum
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = dict()

        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in hashmap:
                return [hashmap[delta], i]

            hashmap[nums[i]] = i
