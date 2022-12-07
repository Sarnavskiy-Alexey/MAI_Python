"""
    Reference: https://www.codewars.com//kata/52423db9add6f6fc39000354
"""


def add_once(cells):
    if sum(cells[0]):
        cells.insert(0, [0] * len(cells[0]))
    if sum(cells[len(cells) - 1]):
        cells.insert(len(cells), [0] * len(cells[0]))
    return cells


def add_empty(cells):
    return list(map(list, zip(*add_once(list(map(list, zip(*add_once(cells))))))))


def delete_once(cells):
    for i in range(len(cells) - 1, -1, -1):
        if not sum(cells[i]):
            cells.pop(i)
        else:
            break
    s = sum(cells[0])
    while s == 0:
        cells.pop(0)
        s = sum(cells[0])
    return cells


def delete_empty(cells):
    return list(map(list, zip(*delete_once(list(map(list, zip(*delete_once(cells))))))))


def get_generation(cells, generations):
    new_cells = [0] * len(cells)
    for i in range(len(new_cells)):
        new_cells[i] = cells[i].copy()

    new_cells = add_empty(new_cells)

    for g in range(generations):
        prev = [0] * len(new_cells)
        for i in range(len(prev)):
            prev[i] = new_cells[i].copy()

        for i in range(len(new_cells)):
            for j in range(len(new_cells[i])):
                neighbours = 0
                neighbours += prev[i + 1][j] if 0 <= i < len(prev) - 1 else 0
                neighbours += prev[i + 1][j + 1] if 0 <= i < len(prev) - 1 and 0 <= j < len(prev[i]) - 1 else 0
                neighbours += prev[i + 1][j - 1] if 0 <= i < len(prev) - 1 and 1 <= j < len(prev[i]) else 0
                neighbours += prev[i][j + 1] if 0 <= j < len(prev[i]) - 1 else 0
                neighbours += prev[i - 1][j] if 1 <= i < len(prev) else 0
                neighbours += prev[i - 1][j - 1] if 1 <= i < len(prev) and 1 <= j < len(prev[i]) else 0
                neighbours += prev[i - 1][j + 1] if 1 <= i < len(prev) and 0 <= j < len(prev[i]) - 1 else 0
                neighbours += prev[i][j - 1] if 1 <= j < len(prev[i]) else 0

                new_cells[i][j] = 1 if not prev[i][j] and neighbours == 3 else new_cells[i][j]
                new_cells[i][j] = 0 if prev[i][j] and (neighbours < 2 or neighbours > 3) else new_cells[i][j]

        for i in range(len(new_cells)):
            for j in range(len(new_cells[i])):
                prev[i][j] = new_cells[i][j]

        new_cells = add_empty(new_cells)

    return delete_empty(new_cells)
