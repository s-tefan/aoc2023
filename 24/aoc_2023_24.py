# AoC 2023, day 20
# S-tefan



import time


def read_input(filename):
    with open(filename) as f:
        it = tuple(line.strip().split('@') for line in f.readlines())
        out = (tuple(tuple(int(c.strip()) for c in post[k].split(',')) for k in range(2)) for post in it)
        return out

def twodet(a,b):
    return a[0]*b[1] - a[1]*b[0]

def cross(a,b):
    return a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]

posts = tuple(read_input('input.txt'))
posmin, posmax = (2*10**14, 4*10**14)
num = 0

for k, post in enumerate(posts): 
    ap, av = post
    #print(post)
    for post2 in posts[:k]:
        #print('*', post2)
        #print(post, post2, twodet(post[1],post2[1]))
        bp, bv = post2
        q = tuple(b-a for (a,b) in zip(ap, bp))
        d = twodet(av[:2],bv[:2])

        if d != 0 :
            t = twodet(q[:2], bv[:2])/d
            s = twodet(q[:2], av[:2])/d
            ip = tuple(p + t*v for p,v in zip(ap, av))
            #print(t, s, ip)
            if all((t >=0, s>=0, posmin <= ip[0] <= posmax, posmin <= ip[1] <= posmax)):
                num +=1
        else:
            #print('no x')
            pass
print(num)