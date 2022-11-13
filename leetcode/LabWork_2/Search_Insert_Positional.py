"""
35. Search Insert Position
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            if target < nums[left]:
                return left
            if target > nums[right]:
                return right + 1

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
