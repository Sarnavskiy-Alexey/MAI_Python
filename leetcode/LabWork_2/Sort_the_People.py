"""
2418. Sort the People
"""


# пузырьковая сортировка
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        length = len(names)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if heights[i] < heights[j]:
                    names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]

        return names
