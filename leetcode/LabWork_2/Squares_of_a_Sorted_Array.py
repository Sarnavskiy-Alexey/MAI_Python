"""
977. Squares of a Sorted Array
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] **= 2

        return self.mergeSort(nums)

    def mergeSort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        part1 = self.mergeSort(data[:mid])
        part2 = self.mergeSort(data[mid:])
        p = []
        i = 0
        j = 0

        while i < len(part1) and j < len(part2):
            if part1[i] < part2[j]:
                p.append(part1[i])
                i += 1
            else:
                p.append(part2[j])
                j += 1
        while i < len(part1):
            p.append(part1[i])
            i += 1
        while j < len(part2):
            p.append(part2[j])
            j += 1
        return p
