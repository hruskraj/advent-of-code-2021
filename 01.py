#!/bin/python3

def get_input():
    with open('./input/1.txt') as f:
        return list(map(int, f.read().splitlines()))
    
def solve(numbers):
    prev = None
    cnt = 0
    
    for curr in numbers:
        if prev:
            cnt = cnt + 1 if curr > prev else cnt
        prev = curr
    return cnt

def group_numbers(numbers):
    out = []
    for i in range(len(numbers) - 2):
        out.append(sum(numbers[i: i + 3]))
    return out

input = get_input()
print(solve(input))
print(solve(group_numbers(input)))
