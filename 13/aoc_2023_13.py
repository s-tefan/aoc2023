# AoC 2023, day 13
# S-tefan

import time



def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def check_symmetry(block):
    n = len(block)
    for m in range(1,n):
        symmetry = True
        for k in range(min(m,n-m)):
            symmetry = symmetry and block[m-k-1] == block[m+k]
            if not symmetry:
                break
        if symmetry:
            return m
    return 0

def transpose(block):
    n = len(block)
    nn = len(block[0])
    return [''.join(block[k][m] for k in range(n)) for m in range(nn)]


def extract_blocks(lines):
    blocks = []
    new_block = []
    for line in lines:
        if line:
            new_block.append(line)
        else:
            if new_block:
                blocks.append(new_block)
                new_block = []
    if new_block:
        blocks.append(new_block)
    return blocks

def parts(lines):
    blocks = extract_blocks(lines)
    s1 = 0
    for block in blocks:
        t = transpose(block)
        symm = 100*check_symmetry(block) + check_symmetry(t)
        s1 += symm

    s2 = 0
    for block in blocks:
        symm1, symm2 = check_symmetry(block), check_symmetry(transpose(block))
        symm = 100*symm1 + symm2
        #n, m = len(block), len(block[0])
        #r1, r2 = range(2*symm1-n, n) if 2*symm1 >= n else range(0, 2*symm1), range(2*symm2-m, m) if 2*symm2 >= m else range(0,2*symm2)
        for m, line in enumerate(block):
            for k, c in enumerate(line):
                li = line
                cleaned_block = [((li[:k] + ('#' if c == '.' else '.') + li[k+1:]) if l == m else li)  for l, li in enumerate(block) ]
                cleaned_symm = 100*check_symmetry(cleaned_block) + check_symmetry(transpose(cleaned_block))
                if cleaned_symm and cleaned_symm != symm:
                    break
            if cleaned_symm and cleaned_symm != symm:
                break
        if cleaned_symm != symm:
            if cleaned_symm//100 == symm // 100:
                ds = cleaned_symm % 100
            elif cleaned_symm % 100 == symm % 100:
                ds = (cleaned_symm // 100) * 100
            else:
                ds = cleaned_symm
        else:
            ds = 0
        print(symm, cleaned_symm, ds)
        s2 += ds
    return s1, s2

    




inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = parts(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
