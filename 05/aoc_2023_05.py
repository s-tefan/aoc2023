class InputError(Exception):
    pass


class Map:
    def __init__(self, iterator):
        self.range = []
        while True:
            title = next(iterator)
            if title:
                break
        a, b = title.split()
        if b != "map:":
            raise InputError("Map title expected")
        self.from_type, _, self.to_type = a.split("-")
        try:
            while True:
                map_line_splits = next(iterator).split()
                if not map_line_splits:
                    raise StopIteration('blank')
                self.range.append(dict(
                    [(['dest', 'source', 'length'][k], int(map_line_splits[k])) for k in range(3)]))
        except StopIteration as exception:
            # print(exception) # Either blank line or end of iterator
            pass


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def parse_input(lines):
    maps = []
    line_iterator = iter(lines)
    line = next(line_iterator)
    splits = line.split()
    if splits[0] == "seeds:":
        seeds = [int(x) for x in splits[1:]]
    else:
        raise InputError("No seeds line")
    try:
        while True:
            new_map = Map(line_iterator)
            maps.append(new_map)
    except StopIteration as exception:
        pass
    return seeds, maps


def partone(lines):
    seeds, maps = parse_input(lines)
    locations = []
    for seed in seeds:
        blupp = seed
        for map in maps:
            got_it = False
            for r in map.range:
                d = blupp - r['source']
                if d in range(r['length']):
                    blupp = r['dest'] + d
                    got_it = True
                    break
            # if not got_it:
                # blupp stays
        locations.append(blupp)

    return min(locations)

# Brute force, funkar men tar evig tid


def parttwo_raw(lines):
    seedranges, maps = parse_input(lines)
    locations = []
    for k in range(len(seedranges)//2):
        seeds = range(seedranges[k], seedranges[k] + seedranges[k+1])
        for seed in seeds:
            blupp = seed
            for map in maps:
                got_it = False
                for r in map.range:
                    d = blupp - r['source']
                    if d in range(r['length']):
                        blupp = r['dest'] + d
                        got_it = True
                        break
                # if not got_it:
                    # blupp stays
            locations.append(blupp)
    return min(locations)

# Funkar, tar några minuter


def parttwo_bw(lines):
    seedranges, maps = parse_input(lines)
    k = 0
    while True:
        m = k
        for map in reversed(maps):
            for r in map.range:
                if m in range(r['dest'], r['dest']+r['length']):
                    m = m + r['source'] - r['dest']
                    break
        for n in range(len(seedranges)//2):
            if m in range(seedranges[2*n], seedranges[2*n] + seedranges[2*n + 1]):
                return k
        k += 1


# Funkar inte korrekt, är väl nån bug nånstans...
def parttwo_delim(lines):
    seedranges, maps = parse_input(lines)
    for map in maps:
        for r in map.range:
            print(seedranges)
            for n in range(len(seedranges)//2):
                if r['source'] in range(seedranges[2*n] + 1, seedranges[2*n] + seedranges[2*n + 1] - 1) \
                        and r['source'] + r['length'] in range(seedranges[2*n] + 1, seedranges[2*n] + seedranges[2*n + 1] - 1):
                    seedranges = (seedranges[:2*n]
                                  + [seedranges[2*n], r['source'] - seedranges[2*n]]
                                  + [r['source'], r['length']]
                                  + [r['source'] + r['length'],
                                     seedranges[2*n] + seedranges[2*n + 1] - (r['source'] + r['length'])]
                                  + seedranges[2*n + 2:])
                elif r['source'] in range(seedranges[2*n] + 1, seedranges[2*n] + seedranges[2*n + 1] - 1):
                    seedranges = (seedranges[:2*n]
                                  + [seedranges[2*n], r['source'] - seedranges[2*n]]
                                  + [r['source'], seedranges[2*n] +
                                     seedranges[2*n + 1] - r['source']]
                                  + seedranges[2*n + 2:])
                elif r['source'] + r['length'] in range(seedranges[2*n] + 1, seedranges[2*n] + seedranges[2*n + 1] - 1):
                    seedranges = (seedranges[:2*n]
                                  + [seedranges[2*n], r['source'] +
                                      r['length'] - seedranges[2*n]]
                                  + [r['source'] + r['length'], seedranges[2*n] +
                                     seedranges[2*n + 1] - r['source'] - r['length']]
                                  + seedranges[2*n + 2:])
                break
            for k, blupp in enumerate(seedranges[::2]):
                got_it = False
                d = blupp - r['source']
                if d in range(r['length']):
                    seedranges[2*k] = r['dest'] + d
                    got_it = True
                    break

    return min(seedranges[::2])


print(partone(read_input("input.txt")))
print(parttwo_bw(read_input("input.txt")))
# print(parttwo_delim(read_input("test.txt")))
