#!/bin/python3

def get_input():
    with open('./input/5.txt') as f:
        return list(map(lambda line: list(map(lambda point: tuple(map(int, point.split(','))), line.split('->'))), f.read().splitlines()))

def get_diagonal_points(x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y1 < y2:
        return [(x1 + i, y1 + i) for i in range(0, x2 - x1 + 1)]
    else:
        return [(x1 + i, y1 - i) for i in range(0, x2 - x1 + 1)]

def get_points(x1, y1, x2, y2, diagonal=False):
    if x1 == x2:
        return [(x1, i) for i in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(i, y1) for i in range(min(x1, x2), max(x1, x2) + 1)]
    elif diagonal:
        return get_diagonal_points(x1, y1, x2, y2)
    else:
        return []

def solve(lines, diagonal=False):
    seen = set()
    unique_lines = set()
    cnt = 0

    for line in lines:
        for point in get_points(*line[0], *line[1], diagonal):
            if point in seen:
                continue
            if point in unique_lines:
                cnt += 1
                seen.add(point)
            else:
                unique_lines.add(point)

    return cnt

input = get_input()
print(solve(input))
print(solve(input, diagonal=True))
