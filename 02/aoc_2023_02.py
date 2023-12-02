import math

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def mupp(s):
    r = s.split(' ')
    return {r[1]: int(r[0])} 

def extract(line):
    meep = line.split(':')
    ap = [k.strip() for k in meep[1].strip().split(';')]
    cep = [[k.strip() for k in bep.split(',')] for bep in ap]
    l = []
    for throw in cep:
        d = {}
        for comp in throw:
            d.update(mupp(comp))
        l.append(d)
    return int(meep[0].split(' ')[1]), l # game #, list of throw dicts

flag = Exception('Hit the fan!')
cubes = {'red': 12, 'green': 13, 'blue': 14}

def partone(lines):
    s = 0
    for line in lines:
        game, throws = extract(line)
        try:
            for th in throws:
                for color in th:
                    if th[color] > cubes[color]:
                        raise flag
        except:
            print(f'{game}, throw {th} is not possible')
        else:
            print(f'{game} is possible')
            s += game
    return s

def parttwo(lines):
    s = 0
    for line in lines:
        game, throws = extract(line)
        max = dict.fromkeys(cubes.keys(), 0)
        for th in throws:
            for color in th:
                if th[color] > max[color]:
                    max[color] = th[color]
        s += math.prod(max.values())
    return s

print(partone(read_input("input.txt")))
print(parttwo(read_input("input.txt")))
