# AoC 2023, day 15
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        return next(line.rstrip().split(',') for line in f.readlines())


print(type(read_input('input.txt')))


def hash(str):
    s = 0
    for c in str:
        s += ord(c)
        s *= 17
        s %= 256
    return s


# 1
print(sum(hash(step) for step in read_input('input.txt')))
