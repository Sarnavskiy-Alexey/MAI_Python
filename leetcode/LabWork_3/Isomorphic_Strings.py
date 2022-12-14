"""
205. Isomorphic Strings
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for ltr in zip(s, t):
            if ltr[0] in d:
                if d[ltr[0]] != ltr[1]:
                    return False
            else:
                d[ltr[0]] = ltr[1]
                if list(d.values()).count(ltr[1]) != 1:
                    return False
        return True
