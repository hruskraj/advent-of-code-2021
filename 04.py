#!/bin/python3
from itertools import groupby
import copy

BOARD_SIZE = 5

class Bingo:
    def __init__(self, board):
        self.board = board
        self.marked = [[False for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        self.finished = False

    def mark(self, number):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == number:
                    self.marked[i][j] = True

    def is_winning(self):
        return any([all(row) for row in self.marked]) or any(all(self.marked[i][j] for i in range(BOARD_SIZE)) for j in range(BOARD_SIZE))

    def is_finished(self):
        return self.finished

    def finish(self):
        self.finished = True

    def get_score(self, number):
        score = 0

        for i in range(BOARD_SIZE):
           for j in range(BOARD_SIZE):
               if not self.marked[i][j]:
                   score += self.board[i][j]

        return score * number

def get_input():
    with open('./input/4.txt') as f:
        data = f.read().splitlines()
        numbers = [int(x) for x in data[0].split(',')]
        tmp = [list(group) for k, group in groupby(data[2:], bool) if k]
        boards = list(map(lambda matrix: [[int(x) for x in row.split()] for row in matrix], tmp))

        return numbers, [Bingo(board) for board in boards]

def solve(numbers, boards, target=1):
    cnt = 0

    for num in numbers:
        for board in boards:
            board.mark(num)

            if not board.is_finished() and board.is_winning():
                cnt += 1
                board.finish()
                if cnt == target:
                    return board.get_score(num)

numbers, boards = get_input()
print(solve(numbers, copy.deepcopy(boards)))
print(solve(numbers, boards, len(boards)))
