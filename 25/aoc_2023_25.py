# AoC 2023, day 20
# S-tefan



import time

class Graph:
    pass

def read_input(filename):
    g = Graph()
    g.vertices = set()
    g.edges = set()
    with open(filename) as f:
        for line in f.readlines():
            it = line.strip().split(':') 
            fr = it[0]
            to = (x.strip() for x in it[1].split())
            g.vertices.add(fr)
            for x in to:
                g.vertices.add(x)
                g.edges.add(frozenset({fr, x}))
    return g

def component(graph, start):
    comp = Graph
    comp.vertices = {start}
    comp.edges = set()
    fringe_edges = {x for x in graph.edges if start in x}
    while fringe_edges:
        fringe = set()
        for edge in fringe_edges:
            fringe.update(edge-comp.vertices)
        comp.vertices.update(fringe)
        comp.edges.update(fringe_edges)
        fringe_edges = set()
        for x in fringe:
            fringe_edges.update(e for e in graph.edges if x in e and e not in comp.edges)
    return comp

g = read_input('test.txt')
print(g.vertices, g.edges)

c = component(g, next(iter(g.vertices)))
print(c.vertices, c.edges)

gg = Graph
gg.vertices = g.vertices
gg.edges = g.edges - {frozenset({'hfx','pzl'}),frozenset({'bvb','cmg'}),frozenset({'nvd','jqt'})}
c = component(gg, next(iter(gg.vertices)))
print(c.vertices, c.edges)
                                                   

