"""
242. Valid Anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = dict()

        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1

        for c in t:
            if c in ds and ds[c] > 0:
                ds[c] -= 1
            else:
                return False

        return not sum(ds.values())
