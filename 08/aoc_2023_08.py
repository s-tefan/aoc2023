# AoC 2023, day 7
# S-tefan
import time, math

class NodeMap:
    def __init__(self, lines):
        self.dest = {}
        self.turn = lines[0]
        for line in lines[1:]:
            if line:
                source, dest_txt = (part.strip() for part in line.split('='))
                self.dest[source] = dict(zip(('L','R'), (x.strip(' ()') for x in dest_txt.split(','))))
        self.pos = 'AAA'
        self.turn_pos = 0
    
    def move(self):
        self.pos = self.dest[self.pos][self.turn[self.turn_pos]]
        self.turn_pos = (self.turn_pos + 1) % len(self.turn)
            
    def move_pos_list(self):
        for k, pos in enumerate(self.pos_list):
            self.pos_list[k] = self.dest[pos][self.turn[self.turn_pos]]
        self.turn_pos = (self.turn_pos + 1) % len(self.turn)


    def distance_to(self, goal):
        d = 0
        while self.pos != goal:
            self.move()
            d += 1
        return d
    
    def set_pos_list(self, pos_list):
        self.pos_list = pos_list 

    def ghost_distance(self): # for part 2
        d = 0
        self.set_pos_list(list(filter(lambda x: x[-1] == 'A', self.dest.keys())))
        #self.pos_list = self.pos_list[:1] # test på del
        dd = d # test
        while any(node[-1] != 'Z' for node in self.pos_list):
            if self.pos_list[1][-1] == 'Z': print(d, d-dd); dd = d # test
            self.move_pos_list()
            d += 1
            #if len(list(filter(lambda x: x[-1] == 'Z',  self.pos_list))) > 2: 
            #print(d, self.pos_list)
        return d

    def ghost_cheat(self): # for part 2
        d = 0
        turn_l = len(self.turn)
        self.set_pos_list(list(filter(lambda x: x[-1] == 'A', self.dest.keys())))
        dd = {} # test
        ap = {}
        while any(node[-1] != 'Z' for node in self.pos_list):
            for node in self.pos_list:
                    if node[-1] == 'Z': 
                        if node in dd.keys():
                            ap[node] = d - dd[node]
                        dd[node] = d

            self.move_pos_list()
            d += 1
            if len(ap) == len(self.pos_list):
                break
        return math.lcm(*ap.values())


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def partone(lines):
    return NodeMap(lines).distance_to('ZZZ')


def parttwo(lines):
    return NodeMap(lines).ghost_distance()

def parttwo_fusk(lines):
    return NodeMap(lines).ghost_cheat()




inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = partone(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
#o = parttwo(inp)
o = parttwo_fusk(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
