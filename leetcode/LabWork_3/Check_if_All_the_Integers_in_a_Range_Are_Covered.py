"""
1893. Check if All the Integers in a Range Are Covered
"""


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        max_el = max([max(el[1], right) for el in ranges])
        seen = [0] * (max_el + 2)

        for l, r in ranges:
            seen[l] += 1
            seen[r + 1] -= 1

        for i in range(1, right + 1):
            seen[i] += seen[i - 1]

        return all(seen[i] for i in range(left, right + 1))
