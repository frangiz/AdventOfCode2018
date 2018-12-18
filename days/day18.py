"""--- Day 18: Settlers of The North Pole ---"""
from helpers import Point, get_adjecent_8
from collections import defaultdict


class LumberCollectionArea():
    def __init__(self, puzzle_input):
        self.area = defaultdict(lambda: '.')
        self.__parse(puzzle_input)
        self.min_x = min(p.x for p in self.area.keys())
        self.max_x = max(p.x for p in self.area.keys())
        self.min_y = min(p.y for p in self.area.keys())
        self.max_y = max(p.y for p in self.area.keys())

    def __parse(self, puzzle_input):
        for y in range(len(puzzle_input)):
            line = puzzle_input[y].strip()
            for x in range(len(line)):
                self.area[Point(x, y)] = line[x]

    def tick(self):
        tmp = {}
        for k, v in self.area.items():
            adjacent_points = get_adjecent_8(k, lambda p: self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y)
            symbols = []
            for p in adjacent_points:
                symbols.append(self.area[p])
            symbols = ''.join(sorted(symbols))
            if v == '.' and '|||' in symbols:
                tmp[k] = '|'
            elif v == '|' and '###' in symbols:
                tmp[k] = '#'
            elif v == '#' and '#' in symbols and '|' in symbols:
                tmp[k] = '#'
            elif v == '#':
                tmp[k] = '.'
            else:
                tmp[k] = v
        for k, v in tmp.items():
            self.area[k] = v

    def draw(self, area):
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                print(area[Point(x, y)], end='')
            print('')
        print('')

    def get_wooded_acres(self):
        return sum(1 for k, v in self.area.items() if v == '|')

    def get_lumberyards(self):
        return sum(1 for k, v in self.area.items() if v == '#')


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    lca = LumberCollectionArea(puzzle_input)
    for _ in range(10):
        lca.tick()
    return str(lca.get_wooded_acres() * lca.get_lumberyards())


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    lca = LumberCollectionArea(puzzle_input)
    seen = {}
    for i in range(1_000_000_000):
        lca.tick()
        state = str(lca.area)
        if state in seen:
            iterations_left = 1_000_000_000 - seen[state] - 1
            pattern_period = i - seen[state]
            for i in range(iterations_left % pattern_period):
                lca.tick()
            break
        seen[state] = i
    return str(lca.get_wooded_acres() * lca.get_lumberyards())


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
