"""
75. Sort Colors
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0] * 3
        for el in nums:
            count_arr[el] += 1
        prefix_sum = [0] * 4
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + count_arr[i - 1]
        for i in range(3):
            for j in range(prefix_sum[i], prefix_sum[i + 1]):
                nums[j] = i
