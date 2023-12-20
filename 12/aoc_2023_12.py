# AoC 2023, day 12
# S-tefan
from math import comb
import time
import sys
#sys.setrecursionlimit(5000)


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def list_of(n, k):
    if k == 0:
        return [[False]*n]
    elif k == n:
        return [[True]*n]
    else:
        first_true = [([True] + a) for a in list_of(n-1, k-1)]
        first_false = [([False] + a) for a in list_of(n-1, k)]
        return first_true + first_false


def components_in_order(b_list):
    p = 0
    l = []
    for b in b_list:
        if b:
            p += 1
        elif p != 0:
            l.append(p)
            p = 0
    if p != 0:
        l.append(p)
    return tuple(l)


def components_no_order(b_list):
    def update(p_dict, p):
        if p:
            if p in p_dict:
                p_dict[p] += 1
            else:
                p_dict[p] = 1

    p_dict = {}
    p = 0
    for b in b_list:
        if b:
            p += 1
        else:
            update(p_dict, p)
            p = 0
    update(p_dict, p)
    return p_dict


def readline(line, part=1):
    '''Funkar för små indata men skalar dåligt'''
    print(line)
    a, b = line.split()
    c = eval(b)
    if part == 2:
        a = '?'.join([a]*5)
        c = c + c + c + c + c
    d = a.count('#')
    n = a.count('?')
    k = sum(c) - d
    l = list_of(n, k)
    no_of_arrs = 0
    for p in l:
        i = iter(p)
        f = [True if m == '#' else False if m ==
             '.' else next(i) if m == '?' else None for m in a]
        if components_in_order(f) == c:
            no_of_arrs += 1
            # print(''.join('#' if x else '.' for x in f), components_in_order(f))
    return no_of_arrs


def greja(list_of_presumptive_components, b):
    '''greja räknar felaktigt med när en presumptiv komponent blir fler'''
    if not list_of_presumptive_components:
        return 1
    else:
        if not b:
            return 0
    num = b[0]
    comp = list_of_presumptive_components[0]
    n, m = comp.count('?'), comp.count('#')
    if len(comp) < num or num < m:
        return greja(list_of_presumptive_components[1:], b)
    else:
        return comb(n, num - m) * greja(list_of_presumptive_components[1:], b[1:]) + greja(list_of_presumptive_components[1:], b)


def arr_count(a, b, bc=0):
    ''' gör nästan rätt men släpper igenom för många'''
    if len(b) == 0:
        if not a and bc == 0:
            print(a, b)
            return 1
        else:
            return 0
    # print(a,b)
    if not a:
        if (not b and bc == 0 or b == [bc]):
            print(a, b)
            return 1
        else:
            return 0
    if a[0] == '?':
        return arr_count('.'+a[1:], b, bc)\
            + arr_count('#'+a[1:], b, bc)  # . alt #
    elif b[0] == bc:
        return (arr_count(a[1:], b[1:], 0) if a[0] == '.' else 0)
    elif a[0] == '.':
        return arr_count(a[1:], b, 0)
    else:  # a[0] == '#'
        return arr_count(a[1:], b, bc+1)


def readline_redux(line, part=1):
    '''greja räknar felaktigt med när en presumptiv komponent blir fler'''
    a, b = line.split()
    b = eval(b)
    if part == 2:
        a = '?'.join([a]*5)
        b = b + b + b + b + b
    list_of_presumptive_components = []
    comp = ''
    for c in a:
        if c == '.':
            if comp:
                list_of_presumptive_components.append(comp)
                comp = ''
        else:
            comp += c
    if comp:
        list_of_presumptive_components.append(comp)
    return greja(list_of_presumptive_components, b)


def readline_redux2(line, part=1):
    a, b = line.split()
    b = list(eval(b))
    if part == 2:
        a = '?'.join([a]*5)
        b = b + b + b + b + b
    return arr_count(a, b)


def partone(lines):
    s = 0
    for line in lines:
        c = readline_redux2(line)
        s += c
        print(f'***{c}')
    return s


def parttwo(lines):
    s = 0
    for line in lines:
        s += readline_redux2(line, 2)
    return s


'''
for p in list_of(5,3):
    print(p, components(p))
'''

inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = partone(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
inp = read_input("test.txt")
a, b = time.perf_counter(), time.process_time()
# o = parttwo(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
