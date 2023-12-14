# AoC 2023, day 14
# S-tefan

import time



def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]



def blupp(n,k):
    r = 1
    for m in range(k):
        r *= (n-m)
    return r

def parts(lines):
    height = len(lines)
    northernmost = [-1]*len(lines[0])
    stones = [{} for k in range(len(lines[0]))] 
    for r, line in enumerate(lines):
        for k, ch in enumerate(line):
            if ch == '#':
                northernmost[k] = r 
            if ch == 'O':
                if northernmost[k] in stones[k]:
                    stones[k][northernmost[k]] += 1
                else:
                    stones[k][northernmost[k]] = 1
    print(stones)
    s = 0
    for stone_comp in stones:
        for n, m in stone_comp.items():
            s += (height - 1 - n)*m -(m-1)*m//2
    print(s)

    




inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = parts(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
