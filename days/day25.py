"""--- Day 25: Four-Dimensional Adventure ---"""
import re


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    points = []
    for line in puzzle_input:
        x, y, z, r = map(int, re.findall(r"([-?\d]+)", line))
        points.append((x, y, z, r))
    constellations = []
    for x, y, z, a in points:
        matching_constellations = []
        for i, c in enumerate(constellations):
            matches = False
            for x2, y2, z2, a2 in c:
                if abs(x2 - x) + abs(y2 - y) + abs(z2 - z) + abs(a2 - a) <= 3:
                    matching_constellations.append(i)
                    matches = True
            if matches:
                c.add((x, y, z, a))
        s = set()
        s.add((x, y, z, a))
        for i in matching_constellations:
            s.update(constellations[i])
            constellations[i].clear()
        constellations.append(s)
    print(constellations)
    return str(sum(len(c) > 0 for c in constellations))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
