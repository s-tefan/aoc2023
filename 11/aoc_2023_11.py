# AoC 2023, day 11
# S-tefan
import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def empty_rows(lines):
    n = []
    for k, line in enumerate(lines):
        if all(c == '.' for c in line):
            n.append(k)
    return n


def empty_cols(lines):
    l = len(lines[0])
    n = []
    for k in range(l):
        if all(line[k] == '.' for r, line in enumerate(lines)):
            n.append(k)
    return n


def galaxies(lines, factor=1):
    e_rows, e_cols = empty_rows(lines), empty_cols(lines)
    g = []
    gg = []
    for r, line in enumerate(lines):
        g += [(r, c) for (c, ch) in enumerate(line) if ch == '#']
    for (r, c) in g:
        rr = r + (factor-1)*[k < r for k in e_rows].count(True)
        cc = c + (factor-1)*[k < c for k in e_cols].count(True)
        gg.append((rr, cc))
    return gg


def partone(lines):
    gals = galaxies(lines)
    dists = []
    for k, g1 in enumerate(gals):
        for g2 in gals[:k]:
            dists.append(abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]))
    return sum(dists)


def parttwo(lines):
    gals = galaxies(lines, 1000000)
    dists = []
    for k, g1 in enumerate(gals):
        for g2 in gals[:k]:
            dists.append(abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]))
    return sum(dists)


inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = partone(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = parttwo(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
