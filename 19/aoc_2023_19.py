# AoC 2023, day 19
# S-tefan

#inte klar än

import time


def read_input(filename):
    with open(filename) as f:
        it = iter(line.rstrip() for line in f.readlines())
        workflows = {}
        while True:
            line = next(it)
            if not line:
                break
            name, b = line.split('{')
            c, _ = b.split('}')
            d = c.split(',')
            workflows[name] = d
        print(workflows)
        parts = []
        try:
            while True:
                line = next(it)
                parts.append(line.strip('{}').split(','))
        except StopIteration:
            pass
        finally:
            pass
        print(parts)
    return workflows, parts

def blarg():
    global mupp, workflows
    while True:
        rapp = workflows[mupp]
        for cond in rapp:
            print(cond)
            if cond == 'A':
                return True
            elif cond == 'R':
                return False
            else:
                if eval(cond):
                    mupp = rapp[cond]
                if mupp == 'R':
                    return False
                elif mupp == 'A':
                    return True
        print(mupp)    


workflows, parts = read_input('test.txt')
for part in parts:
    print(part)
    for ap in part:
        exec(ap)
        mupp = 'in'
        blarg()
