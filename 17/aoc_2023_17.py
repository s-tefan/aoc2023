# AoC 2023, day 17
# S-tefan

'''
Felet för tillfället tror jag är att en partiell stig som är kortast till en punkt inte
nödvändigtvis är sterten på den kortaste till mål, om den då skulle behöva fortsättas
i en otillåten rät linje. 
'''

import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


class Node:
    def __init__(self, pos, path = []):
        self.pos = pos
        self.path = path
    
    def next(self, rs, cs):
        out = set()
        r, c = self.pos
        for (dr, dc) in ((1,0),(-1,0),(0,1),(0,-1)):
            if all((r+dr < rs, r+dr >= 0, c+dc < cs, c+dc >=0)):
                '''
                if (dr,dc) == self.straight and self.to_go_straight:
                    out.add(Node((r+dr, c+dc), straight = (dr,dc), to_go_straight = self.to_go_straight - 1)) 
                elif not (self.straight and self.straight[0] == -dr and self.straight[1] == -dc):
                    out.add(Node((r+dr, c+dc), straight = (dr,dc)))
                '''
                if not ((len(self.path) >= 3 and all(self.path[-k].pos == (r - k*dr, c) for k in range(1,4))) \
                    or (len(self.path) >= 3 and all(self.path[-k].pos == (r, c - k*dc) for k in range(1,4))) \
                        or (len(self.path) >= 1 and self.path[-1].pos == (r+dr,c+dc))):
                    out.add(Node((r+dr, c+dc), path = self.path + [self]))
                        
        #print([(x.pos) for x in out])
        return out
    
    
    def __hash__(self):
        return hash((self.pos, tuple(self.path[-3:])))
        
    def __eq__(self, other):
        return hash(self.pos) == hash(self.other)
    
def dijkstra(grid):
    rs, cs = len(grid), len(grid[0])
    current = Node((0,0))
    dist_dict = {current: 0}
    visited = {current}
    dest = Node((rs-1,cs-1))

    while not any(x.pos == (rs-1,cs-1) for x in visited):
    #while not dest in visited:
        #print([x.pos for x in visited])
        #print('*',current.pos, dist_dict[current], [x.pos for x in current.path], path[current])
        #time.sleep(0.5)
        tentative_set = current.next(rs, cs).difference(visited)
        tentative_dict = {t: dist_dict[current] + int(grid[t.pos[0]][t.pos[1]]) for t in tentative_set}
        for t in tentative_set:
            if t in dist_dict.keys():
                if tentative_dict[t] < dist_dict[t]:
                    dist_dict[t] = tentative_dict[t]
            else:
                dist_dict[t] = tentative_dict[t]
        visited.add(current)
        if set(dist_dict).difference(visited):
            current = min(set(dist_dict).difference(visited), key = lambda x: dist_dict[x])
        else: 
            print('Hallabaloo')
    return dist_dict[dest]
            
grid = read_input('test.txt')
print(dijkstra(grid))











