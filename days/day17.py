"""--- Day 17: Reservoir Research ---"""
from helpers import Point
import re


def simulate_flow(puzzle_input):
    clay = set()
    for line in puzzle_input:
        a, b, c = map(int, re.findall(r"([\d]+)", line))
        if line.startswith('x'):
            for y in range(b, c + 1):
                clay.add(Point(a, y))
        else:
            for x in range(b, c + 1):
                clay.add(Point(x, a))
    lowest_y = max(p.y for p in clay)
    water_spring = Point(500, 0)
    still = set()
    flowing = set()
    to_fall = set()
    to_spread = set()

    to_fall.add(water_spring)
    while to_fall or to_spread:
        while to_fall:
            falling_point = to_fall.pop()
            res = fall(falling_point, lowest_y, clay, flowing)
            if res:
                to_spread.add(res)
        while to_spread:
            spreading_point = to_spread.pop()
            res_left, res_right = spread(spreading_point, clay, flowing, still)
            if not res_left and not res_right:
                to_spread.add(Point(spreading_point.x, spreading_point.y - 1))
            else:
                if res_left:
                    to_fall.add(res_left)
                if res_right:
                    to_fall.add(res_right)
    return flowing, still, clay


def fall(pos, lowest_y, clay, flowing):
    while pos.y < lowest_y:
        pos_down = Point(pos.x, pos.y + 1)
        if pos_down not in clay:
            flowing.add(pos_down)
            pos = pos_down
        elif pos_down in clay:
            return pos
    return None


def spread(pos, clay, flowing, still):
    tmp = set()
    pl = spread_vertical(pos, Point(-1, 0), clay, still, tmp)
    pr = spread_vertical(pos, Point(1, 0), clay, still, tmp)
    if not pl and not pr:
        still.update(tmp)
    else:
        flowing.update(tmp)
    return pl, pr


def spread_vertical(pos, off, clay, still, tmp):
    pos1 = pos
    while pos1 not in clay:
        tmp.add(pos1)
        pos2 = Point(pos1.x, pos1.y + 1)
        if pos2 not in clay and pos2 not in still:
            return pos1
        pos1 = Point(pos1.x + off.x, pos1.y + off.y)
    return None


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    flowing, still, clay = simulate_flow(puzzle_input)
    highest_y = min(p.y for p in clay)
    return str(len([p for p in flowing | still if p.y >= highest_y]))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    _, still, clay = simulate_flow(puzzle_input)
    highest_y = min(p.y for p in clay)
    return str(len([p for p in still if p.y >= highest_y]))


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
