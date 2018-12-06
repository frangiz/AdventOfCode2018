"""--- Day 06: Chronal Coordinates ---"""
import helpers
from collections import defaultdict


def find_closest(pos, locations):
    distances = defaultdict(list)
    for loc in locations:
        distance = helpers.get_manhattan_dist(pos, loc)
        distances[distance].append(loc)
    min_key = min(distances.keys())
    if len(distances[min_key]) == 1:
        return distances[min_key][0]
    return None


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    locations = []
    regions = defaultdict(int)
    inf_regions = set()
    for line in puzzle_input:
        x, y = line.split(', ')
        locations.append(helpers.Point(int(x), int(y)))
    min_x = min(locations, key=lambda p: p.x).x
    max_x = max(locations, key=lambda p: p.x).x
    min_y = min(locations, key=lambda p: p.y).y
    max_y = max(locations, key=lambda p: p.y).y
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = helpers.Point(x, y)
            closest = find_closest(p, locations)
            if closest is not None:
                regions[closest] += 1
                if p.x == min_x or p.x == max_x or p.y == min_y or p.y == max_y:
                    inf_regions.add(closest)
    return str(max(size for r, size in regions.items() if r not in inf_regions))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    locations = []
    for line in puzzle_input:
        x, y = line.split(', ')
        locations.append(helpers.Point(int(x), int(y)))
    min_x = min(locations, key=lambda p: p.x).x
    max_x = max(locations, key=lambda p: p.x).x
    min_y = min(locations, key=lambda p: p.y).y
    max_y = max(locations, key=lambda p: p.y).y
    safe_region_size = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = helpers.Point(x, y)
            s = 0
            for loc in locations:
                s += helpers.get_manhattan_dist(p, loc)
            if s < 10_000:  # TODO: < have to be a parameter somehow -> 32 for the example
                safe_region_size += 1
    return str(safe_region_size)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
