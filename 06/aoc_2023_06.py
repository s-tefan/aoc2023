
def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def partone(lines):
    times_s, distances_s = (line.split()[1:] for line in lines)
    p = 1
    for k, time_s in enumerate(times_s):
        time, distance = int(time_s), int(distances_s[k])
        m = (time + 1) % 2
        d = time**2 - 4*distance
        while (m-1)**2 < d:
            m += 2
        print(m-2)
        p *= (m-2)
    return p

def parttwo(lines):
    time, distance = (int(''.join(filter(lambda x: x != ' ', line.split(None, 1)[1]))) for line in lines)
    m = (time + 1) % 2
    d = time**2 - 4*distance
    while (m-1)**2 < d:
        m += 2
    return m-2


print(partone(read_input("input.txt")))
print(parttwo(read_input("input.txt")))
