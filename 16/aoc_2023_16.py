# AoC 2023, day 16
# S-tefan

import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


class Grid:
    def __init__(self, basegrid):
        self.basegrid = basegrid
        self.energized = set()
        self.passed = set()

    def reset(self):
        self.energized = set()
        self.passed = set()


class Beam:
    def __init__(self, grid, position=(0, 0), direction=(0, 1)):
        self.grid = grid
        self.position = position
        self.direction = direction

    def run(self):
        self.running = True
        while self.running:
            self.step()
        return len(self.grid.energized)

    def stop(self):
        self.running = False

    def step(self):
        if self.out_of_bounds():
            self.stop()
            return
        r, c = self.position
        match self.grid.basegrid[r][c]:
            case '.':
                self.move()
            case '|':
                if self.direction in {(0, 1), (0, -1)}:
                    self.split(direction=(1, 0))
                    self.direction = (-1, 0)
                    self.move()
                else:
                    self.move()
            case '-':
                if self.direction in {(1, 0), (-1, 0)}:
                    self.split(direction=(0, 1))
                    self.direction = (0, -1)
                    self.move()
                else:
                    self.move()
            case '/':
                match self.direction:
                    case (1, 0):
                        self.direction = (0, -1)
                    case (-1, 0):
                        self.direction = (0, 1)
                    case (0, 1):
                        self.direction = (-1, 0)
                    case (0, -1):
                        self.direction = (1, 0)
                self.move()
            case '\\':
                match self.direction:
                    case (1, 0):
                        self.direction = (0, 1)
                    case (-1, 0):
                        self.direction = (0, -1)
                    case (0, 1):
                        self.direction = (1, 0)
                    case (0, -1):
                        self.direction = (-1, 0)
                self.move()
            case _:
                raise Error('Blöh')

    def out_of_bounds(self):
        r, c = self.position
        return r < 0 or r >= len(self.grid.basegrid) \
            or c < 0 or c >= len(self.grid.basegrid[r])

    def move(self):
        self.grid.energized.add(self.position)
        if (self.position, self.direction) in self.grid.passed:
            self.stop()
            return
        self.grid.passed.add((self.position, self.direction))
        r, c = self.position
        dr, dc = self.direction
        self.position = (r+dr, c+dc)

    def split(self, direction):
        # print('Splitting!')
        split_beam = Beam(self.grid)
        split_beam.position = self.position
        split_beam.direction = direction
        split_beam.move()  # not to interfer by energizing
        split_beam.run()


# 1
grid = Grid(read_input('input.txt'))
beam = Beam(grid)
print(beam.run())
# 2
m = 0
for k in range(len(grid.basegrid)):
    grid.reset()
    beam = Beam(grid, position=(k, 0), direction=(0, 1))
    m = max(m, beam.run())
    grid.reset()
    beam = Beam(grid, position=(k, len(grid.basegrid[k])-1), direction=(0, -1))
    m = max(m, beam.run())
for k in range(len(grid.basegrid[0])):
    grid.reset()
    beam = Beam(grid, position=(0, k), direction=(1, 0))
    m = max(m, beam.run())
    grid.reset()
    beam = Beam(grid, position=(len(grid.basegrid)-1, k), direction=(-1, 0))
    m = max(m, beam.run())
print(m)
