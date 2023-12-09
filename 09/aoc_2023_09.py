# AoC 2023, day 7
# S-tefan
import time



def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def partone(lines):
    s = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        diffs = [vals]
        n = 0
        while any(diffs[n]) != 0:
            diffs.append([diffs[n][k+1] - diffs[n][k] for k in range(len(diffs[n]) - 1)])
            n += 1
        new_val = 0
        for k in reversed(range(n)):
            new_val = new_val + diffs[k][-1]
        s += new_val
    return s

def parttwo(lines):
    s = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        diffs = [vals]
        n = 0
        while any(diffs[n]) != 0:
            diffs.append([diffs[n][k+1] - diffs[n][k] for k in range(len(diffs[n]) - 1)])
            n += 1
        new_val = 0
        for k in reversed(range(n)):
            new_val = diffs[k][0] - new_val
        s += new_val
    return s


inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = partone(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = parttwo(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
