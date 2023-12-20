# AoC 2023, day 20
# S-tefan

# funkar inte riktigt, tänk igenom hur det ska vara

import time


def read_input(filename):
    with open(filename) as f:
        it = (line.strip().split(' -> ') for line in f.readlines())
    return it

class Module:
    @staticmethod
    def create(conf):
        if conf[0] == 'broadcaster':
            new_module = Broadcaster(conf)
        elif conf[0] == 'button':
            new_module = Button(conf)
        elif conf[0][0] == '%':
            new_module = FlipFlop(conf)
        elif conf[0][0] == '&':
            new_module = Conjunction(conf)
        return new_module

    # ska man ha ett slags register som klassvariabel, kanske?
    def __init__(self, conf):
        self.targets = [k.strip() for  k in  conf[1].split(',')]

class Broadcaster(Module):
    def __init__(self, conf):
        self.label = conf[0]
        Module.__init__(self, conf)
    def action(self, input):
        return [input for _ in self.targets]

class FlipFlop(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        self.state = False
        Module.__init__(self, conf)
    def action(self, input):
        if input:
            return None
        else: 
            self.state ^= True # toggle 
            return self.state,

class Conjunction(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        Module.__init__(self, conf)
        self.state = {k: False for k in self.targets}
    def action(self, input):
        self.state[input['label']] = input['value']
        return not all(self.state.values()),

class Button(Module):    
    def __init__(self, conf):
        self.label = conf[0][1:]
        Module.__init__(self, conf)
    def action(self, input):
        pass


modules = {}
for conf in read_input('test.txt'):
    m = Module.create(conf)
    print(type(m), m.label, m.targets, (m.state if hasattr(m, 'state') else ''))
    modules[m.label] =  m
mlist = ['module': modules['broadcast'], 'in': , True]
while mlist:
    m = mlist.pop(0)
    pulses = m['module'].action(m['in'])
    mlist += zip(m.targets, m.pulses)
    print(mlist)
