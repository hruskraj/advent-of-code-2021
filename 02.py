#!/bin/python3

def get_input():
    with open('./input/2.txt', 'r') as f:
        l = map(lambda x: tuple(x.split()), f.readlines())
        return list(map(lambda x: (x[0], int(x[1])), l))

def solve(commands, second = 0):
    horizontal = depth = aim = 0

    for command in  commands:
        if command[0] == 'forward':
            horizontal += command[1]
            depth += command[1] * aim * second
        elif command[0] == 'up':
            depth -= command[1] * (1 - second)
            aim -= command[1] * second
        else:
            depth += command[1] * (1 - second)
            aim += command[1] * second

    return depth * horizontal

input = get_input()
print(solve(input))
print(solve(input, second=1))
