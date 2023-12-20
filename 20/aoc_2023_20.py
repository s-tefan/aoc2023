# AoC 2023, day 20
# S-tefan

# funkar inte riktigt med underklasserna som jag först tänkt
# ska kanske bara ha Module och ha olika actions beroende på modultyp

import time


def read_input(filename):
    with open(filename) as f:
        it = (line.strip().split(' -> ') for line in f.readlines())
    return it

class Module:
    # ska man ha ett slags register som klassvariabel, kanske?
    def __init__(self, conf):
        self.targets = [k.strip() for  k in  conf[1].split(',')]
        if conf[0] == 'broadcaster':
            self = Broadcaster(conf)
        elif conf[0] == 'button':
            self = Button(conf)
        elif conf[0][0] == '%':
            self = FlipFlop(conf)
        elif conf[0][0] == '&':
            self = Conjunction(conf)

class Broadcaster(Module):
    def __init__(self, conf):
        self.label = conf[0]
        pass

    def action(self, input):
        pass

class FlipFlop(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        pass
    def action(self, input):
        pass

class Conjunction(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        pass
    def action(self, input):
        pass

class Button(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        pass
    def action(self, input):
        pass


modules = set()
for conf in read_input('test.txt'):
    m = Module(conf)
    print(m.label, m.targets)
    modules.add(Module(conf))

