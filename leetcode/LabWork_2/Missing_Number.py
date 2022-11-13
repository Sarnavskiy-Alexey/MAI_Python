"""
268. Missing Number
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2

            if left == mid:
                return mid + 1

            if mid - left != nums[mid] - nums[left]:
                right = mid
            elif right - mid != nums[right] - nums[mid]:
                left = mid
