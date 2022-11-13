"""
1539. Kth Missing Positive Number
"""

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        all_missed = arr[len(arr) - 1] - len(arr)

        if k < arr[0]:
            return k
        if k > all_missed:
            return arr[len(arr) - 1] + (k - all_missed)

        left = 0
        right = len(arr) - 1
        miss = arr[left] - 1

        while left < right:
            mid = (right + left) // 2
            cur_miss = arr[mid] - arr[left] - (mid - left)

            if left == mid:
                return arr[left] + k - miss

            if not cur_miss:
                left = mid
            else:
                if miss + cur_miss < k:
                    left = mid
                    miss += cur_miss
                else:
                    right = mid
