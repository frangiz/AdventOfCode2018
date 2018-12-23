"""--- Day 23: Experimental Emergency Teleportation ---"""
import re
import operator


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    nanobots = []
    for line in puzzle_input:
        x, y, z, r = map(int, re.findall(r"([-\d]+)", line))
        nanobots.append((x, y, z, r))

    within_range = 0
    bb_x, bb_y, bb_z, bb_r = max(nanobots, key=operator.itemgetter(3))
    for bot in nanobots:
        x, y, z, r = bot
        if (abs(x - bb_x) + abs(y - bb_y) + abs(z - bb_z)) <= bb_r:
            within_range += 1
    return str(within_range)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    nanobots = []
    for line in puzzle_input:
        x, y, z, r = map(int, re.findall(r"([-\d]+)", line))
        nanobots.append((x, y, z, r))

    print('bah!')

    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
