# AoC 2023, day 20
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        it = iter(line.strip().split(' - > ') for line in f.readlines())

class Module:
    # ska man ha ett slags register som klassvariabel, kanske?
    def __init__(self, conf):
        if conf[0] == 'broadcaster':
            return Broadcaster(conf)
        elif conf[0] == 'button':
            return Button(conf)
        elif conf[0][0] == '%':
            return FlipFlop(conf)
        elif conf[0][0] == '&':
            return Conjunction(conf)

class Broadcaster(Module):
    def __init__(self, conf):
        self.targets = tuple(x.split(',').strip() for x in conf[1])
    
    def action(self, input):


