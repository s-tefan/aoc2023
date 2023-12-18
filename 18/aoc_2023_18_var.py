# AoC 2023, day 18
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip().split() for line in f.readlines()]


posts = read_input("input.txt")
dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}


# 1
r, c, s, a = 0, 0, 0, 0
for post in posts:
    ds = int(post[1])
    dr, dc = (ds*x for x in dirs[post[0]])
    r1, c1 = r + dr, c + dc
    a += (r1*c - c1*r)
    r, c = r1, c1
    s += ds
a = (abs(a) + s + 2)//2
print(a)

# 2
newdirs = [dirs[x] for x in 'RDLU']
r, c, s, a = 0, 0, 0, 0
for post in posts:
    ds = int(post[2][2:7], 16)
    dr, dc = (ds*x for x in newdirs[int(post[2][7])])
    r1, c1 = r + dr, c + dc
    a += (r1*c - c1*r)
    r, c = r1, c1
    s += ds
a = (abs(a) +  s + 2)//2
print(a)
