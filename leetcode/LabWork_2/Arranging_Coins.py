"""
441. Arranging Coins
"""

def countStairsByNum(n: int) -> int:
    s = n * ((n + 1) / 2)
    return int(s)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        mid = 1

        while left < right:
            mid = (right + left) // 2
            if countStairsByNum(mid) == n or left == mid or right == mid:
                return mid

            if countStairsByNum(mid) > n:
                right = mid
            elif countStairsByNum(mid) <= n:
                left = mid
        return mid
