"""
128. Longest Consecutive Sequence
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        max_longest = 0

        for el in nums:
            if el - 1 not in s:
                counter = 1
                while el + counter in s:
                    counter += 1
                max_longest = max(max_longest, counter)
        return max_longest
