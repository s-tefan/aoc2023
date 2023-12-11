# AoC 2023, day 10
# S-tefan
import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


connector_dict = {'|': {(-1, 0), (1, 0)},
                  '-': {(0, -1), (0, 1)},
                  'L': {(-1, 0), (0, 1)},
                  'J': {(-1, 0), (0, -1)},
                  '7': {(1, 0), (0, -1)},
                  'F': {(0, 1), (1, 0)},
                  '.': {}
                  }


def get(lines):
    pipes = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == 'S':
                start = (r, c)
                nearest = {}
                ap = set()
                if r > 0 and lines[r-1][c] in '|F7':
                    ap.add((-1, 0))
                    nearest[r-1, c] = 1
                if r < len(lines) - 1 and lines[r+1][c] in '|JL':
                    ap.add((1, 0))
                    nearest[r+1, c] = 1
                if c > 0 and line[c-1] in '-LF':
                    ap.add((0, -1))
                    nearest[r, c-1] = 1
                if c < len(line) - 1 and line[c+1] in '-J7':
                    ap.add((0, 1))
                    nearest[r, c+1] = 1
                for k, v in connector_dict.items():
                    if v == ap:
                        lines[r] = line[:c]+k+line[c+1:]
            elif char in connector_dict:
                pipes[(r, c)] = char
    return pipes, start, nearest


def neighbors(lines, pos):
    r, c = pos
    char = lines[r][c]
    b = connector_dict[char]
    nbs = set()
    for n in b:
        rr, cc = n
        if r+rr in range(len(lines)) and c+cc in range(len(lines[r])):
            nbs.add((r+rr, c+cc))
    return nbs


def partonetwo(lines):
    pipes, start, nearest = get(lines)
    sr, sc = start
    visited = {start: 0}
    last_visited = {k: 1 for k in nearest}
    visited.update(last_visited)
    break_it = False
    while not break_it:
        newly_visited = {}
        for l in last_visited:
            for k in neighbors(lines, l).difference(visited.keys()):
                newly_visited[k] = visited[l] + 1
            if not newly_visited:
                result_one = visited[l]
                break_it = True
            last_visited = newly_visited
            visited.update(last_visited)

    rmin = min(r for r, c in visited.keys())
    rmax = max(r for r, c in visited.keys())
    inners = []
    for r in range(rmin + 1, rmax):
        flag, F, L = False, False, False
        for c, ch in enumerate(lines[r]):
            if (r, c) in visited.keys():
                if ch == '|':
                    flag = not flag
                elif ch == 'F':
                    F = True
                elif ch == 'L':
                    L = True
                elif F:
                    if ch == 'J':
                        flag = not flag
                        F = False
                    if ch == '7':
                        F = False
                elif L:
                    if ch == '7':
                        flag = not flag
                        L = False
                    if ch == 'J':
                        L = False
            else:
                if flag:
                    inners.append((r, c))
    result_two = len(inners)
    return result_one, result_two


def parttwo(lines):
    return None


inp = read_input("input.txt")
a, b = time.perf_counter(), time.process_time()
o = partonetwo(inp)
print(o, time.perf_counter()-a, time.process_time()-b)
