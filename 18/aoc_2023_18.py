# AoC 2023, day 18
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip().split() for line in f.readlines()]


posts = read_input("input.txt")
trench = [(0, 0)]
dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

r, c, s, a = 0, 0
for post in posts:
    ds = int(post[1])
    dr, dc = (ds*x for x in dirs[post[0]])
    r, c = r + dr, c + dc
    a += c*dr
    s += ds
print(a)
a += (s + 2)//2
print(a)
