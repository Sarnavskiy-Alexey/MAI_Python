"""
278. First Bad Version
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = 0
        while left <= right:
            mid = (right + left) // 2

            if left == right:
                return left

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return mid
