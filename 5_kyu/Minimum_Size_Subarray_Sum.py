"""
    Взамен задачи https://www.codewars.com//kata/5a5c5a1ab3bfa8728d00008d
    Reference: https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1] + nums[i - 1]
        if target > prefix_sum[-1]:
            return 0
        
        left = 0
        min_len = len(prefix_sum) + 1
        
        for right in range(1, len(prefix_sum)):
            while prefix_sum[right] - prefix_sum[left] >= target:
                min_len = min(min_len, right - left)
                left += 1
        return min_len


def launch_test(target: int, nums: list, answer: int):
    print(Solution().minSubArrayLen(target, nums), '==', answer)


if __name__ == '__main__':
    launch_test(7, [2, 3, 1, 2, 4, 3], 2)
    launch_test(4, [1, 4, 4], 1)
    launch_test(11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
    launch_test(11, [1, 2, 3, 4, 5], 3)
    launch_test(15, [1, 2, 3, 4, 5], 5)
