"""--- Day 10: The Stars Align ---"""
import helpers


class Point():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return '({}, {} -> {}, {})'.format(self.x, self.y, self.dx, self.dy)

    def tick(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy


def parse(puzzle_input):
    points = []
    for line in puzzle_input:
        parts = line[len('position=<'):].strip().split('> velocity=<')
        x, y = parts[0].split(',')
        dx, dy = parts[1][:-1].split(',')
        points.append(Point(int(x), int(y), int(dx), int(dy)))
    return points


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    points = parse(puzzle_input)

    for _ in range(100_000):
        min_x = min(points, key=lambda p: p.x).x
        max_x = max(points, key=lambda p: p.x).x
        min_y = min(points, key=lambda p: p.y).y
        max_y = max(points, key=lambda p: p.y).y

        if abs(max_y - min_y) < 20:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if any(p.x == x and p.y == y for p in points):
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')
            print('-' * 50)
        for p in points:
            p.tick()
    return str(0)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    points = parse(puzzle_input)
    time = 0

    for _ in range(100_000):
        min_x = min(points, key=lambda p: p.x).x
        max_x = max(points, key=lambda p: p.x).x
        min_y = min(points, key=lambda p: p.y).y
        max_y = max(points, key=lambda p: p.y).y

        if abs(max_y - min_y) < 20:
            print(time)
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if any(p.x == x and p.y == y for p in points):
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')
            print('-' * 50)
        for p in points:
            p.tick()
        time += 1
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
