"""--- Day 06: Chronal Coordinates ---"""
import helpers
from collections import defaultdict


def parse_locations(puzzle_input):
    locations = []
    for line in puzzle_input:
        x, y = line.split(', ')
        locations.append(helpers.Point(int(x), int(y)))
    min_x = min(locations, key=lambda p: p.x).x
    max_x = max(locations, key=lambda p: p.x).x
    min_y = min(locations, key=lambda p: p.y).y
    max_y = max(locations, key=lambda p: p.y).y
    return (locations, min_x, max_x, min_y, max_y)


def find_closest(pos, locations):
    min_dist = 10**5
    closest_loc = None
    for loc in locations:
        dist = abs(pos.x - loc.x) + abs(pos.y - loc.y)
        if dist < min_dist:
            min_dist = dist
            closest_loc = loc
        elif dist == min_dist:
            closest_loc = None
    return closest_loc


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    locations, min_x, max_x, min_y, max_y = parse_locations(puzzle_input)
    regions = defaultdict(int)
    inf_regions = set()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            p = helpers.Point(x, y)
            closest = find_closest(p, locations)
            if closest is not None:
                regions[closest] += 1
                if p.x == min_x or p.x == max_x or p.y == min_y or p.y == max_y:
                    inf_regions.add(closest)
    return str(max(size for region, size in regions.items() if region not in inf_regions))


def part_b(puzzle_input, safe_distance=10_000):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    locations, min_x, max_x, min_y, max_y = parse_locations(puzzle_input)
    safe_region_size = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            s = sum(abs(x - loc.x) + abs(y - loc.y) for loc in locations)
            if s < safe_distance:
                safe_region_size += 1
    return str(safe_region_size)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
