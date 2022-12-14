"""
15. 3Sum
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        history = set()
        quadruplet = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    delta = target - nums[i] - nums[j] - nums[k]
                    if delta in history:
                        quadruplet.add((delta, nums[i], nums[j], nums[k]))
            history.add(nums[i])
        return quadruplet
