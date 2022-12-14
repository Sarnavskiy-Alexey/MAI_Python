"""
49. Group Anagrams
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = dict()
        for el in strs:
            hashsum = 0
            for letter in el:
                hashsum += hash(letter)
            if hashsum not in d:
                d[hashsum] = []
            d[hashsum] += [el]
        return list(d.values())
