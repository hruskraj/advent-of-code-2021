#!/bin/python3
from statistics import mode

def get_input():
    with open('./input/3.txt') as f:
        return list(f.read().splitlines())

def part_1(numbers):
    length = len(numbers[0])
    gamma = ''

    for i in range(length):
        gamma += mode(map(lambda x: x[i], numbers))
    epsilon = ''.join(map(lambda x: str(1 - int(x)), gamma))

    return int(gamma, 2) * int(epsilon, 2)

def most_common(t, i, rating):
    cnt = list(map(lambda x: x[i], t)).count(rating)
    return rating if len(t) - cnt <= cnt else str(1 - int(rating))

def least_common(t, i, rating):
    cnt = list(map(lambda x: x[i], t)).count(rating)
    return rating if len(t) - cnt >= cnt else str(1 - int(rating))

def get_rating(numbers, common_fun, rating):
    length = len(numbers[0])

    for i in range(length):
        cmn = common_fun(numbers, i, rating)
        numbers = [num for num in numbers if num[i] == cmn]
        if len(numbers) == 1:
            return int(numbers[0], 2)

def part_2(numbers):
    return get_rating(numbers, most_common, '1') * get_rating(numbers, least_common, '0')

input = get_input()
print(part_1(input))
print(part_2(input))
