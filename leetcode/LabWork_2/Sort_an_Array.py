"""
912. Sort an Array
"""

# Сортировка слиянием
def MergeSort(data: list[int]):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    part1 = MergeSort(data[:mid])
    part2 = MergeSort(data[mid:])
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


# Сортировка подсчетом
def CountingSort(self, data: list[int]) -> list[int]:
    max_k = max(data)
    min_k = min(data)
    l = [0] * (max_k - min_k + 1)
    for i in data:
        l[i - min_k] += 1
    result = []
    for i in range(len(l)):
        if l[i] > 0:
            result += [i + min_k] * l[i]

    return result


# Быстрая сортировка
def QuickSort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    elif len(data) == 2 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]
        return data

    mid = len(data) // 2

    left, middle, right = QuickPart(data, mid)

    return left + middle + right


# Разбиение для быстрой сортировки
def QuickPart(data: list[int], mid: int):
    left = []
    middle = []
    right = []
    for i in data:
        if i < data[mid]:
            left.append(i)
        elif i > data[mid]:
            right.append(i)
        else:
            middle.append(i)

    return QuickSort(left), middle, QuickSort(right)


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # return MergeSort(nums)
        # return CountingSort(nums)
        # return QuickSort(nums)
        pass
