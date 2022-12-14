"""
560. Subarray Sum Equals K
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        d = {0: 1}
        prefix_sum = 0
        counter = 0

        for el in nums:
            prefix_sum += el
            if prefix_sum - k in d:
                counter += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1

        return counter
