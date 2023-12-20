# AoC 2023, day 14
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def part_one(lines):
    height = len(lines)
    northernmost = [height]*len(lines[0])  # avståndet från söder under klossen
    stones = [{} for k in range(len(lines[0]))]
    for r, line in enumerate(lines):
        for k, ch in enumerate(line):
            if ch == '#':
                northernmost[k] = height - r - 1
            if ch == 'O':
                if northernmost[k] in stones[k]:
                    stones[k][northernmost[k]] += 1
                else:
                    stones[k][northernmost[k]] = 1
    s = 0
    for stone_comp in stones:
        for n, m in stone_comp.items():
            s += (2*n-m+1)*m//2
    return s


def transpose(block):
    n = len(block)
    nn = len(block[0])
    return [''.join(block[k][m] for k in range(n)) for m in range(nn)]


def rotate(block):
    n1 = len(block)
    n2 = len(block[0])
    return [''.join(block[m][n2-k-1] for m in range(n1)) for k in range(n2)]


def move(ap):
    bep = []
    for line in ap:
        os, pos = 0, 0
        new_line = ''
        for k, c in enumerate(line):
            if c == 'O':
                os += 1
            if c == "#":
                new_line += ('O'*os + '.'*(k-pos-os) + '#')
                pos = k + 1
                os = 0
        new_line += ('O'*os + '.'*(k + 1 - pos - os))
        bep.append(new_line)
    return bep


def cycle(ap):
    for turn in range(4):
        ap = rotate(move(ap))
    return ap


def hash(ap):
    h = 0
    k = 0
    for line in ap:
        for c in line:
            if c == 'O':
                h += 3**k
            elif c == '#':
                h += 2*3**k
            k += 1
    return h


def equal(ap, bep):
    return all(ap[k] == bep[k] for k, _ in enumerate(ap))


def load(ap):
    l = len(ap[0])
    return sum(sum(l-k if c == 'O' else 0 for k, c in enumerate(line)) for line in ap)


def part_two(lines):
    ap = transpose(lines)
    # norr är nu "till vänster", väster "överst", dvs första raden västligast, med första tecknet nordligast
    k = 0
    hashes = []
    for k in range(10**9):
        h = hash(ap)
        if h in hashes:
            per = list(reversed(hashes)).index(h) + 1
            break
        hashes.append(h)
        ap = cycle(ap)
    print(k, per, load(ap))
    slut = 10**9
    for m in range((slut-k) % per):
        ap = cycle(ap)
    return load(ap)


def test(lines):
    ap = transpose(lines)
    # norr är nu "till vänster", väster "överst", dvs första raden västligast, med första tecknet nordligast
    print(load(move(ap)))
    for k in range(20):
        print(ap)
        print(k, hash(ap), load(ap))
        ap = cycle(ap)


inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = part_one(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
a, b = time.perf_counter(), time.process_time()
o = part_two(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
# test(read_input("test.txt"))
