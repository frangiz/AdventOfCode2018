"""--- Day 07: The Sum of Its Parts ---"""
from collections import defaultdict
import string


def parse_deps(puzzle_input):
    deps = defaultdict(set)
    for line in puzzle_input:
        parts = line.split()
        deps[parts[7]].add(parts[1])
    return deps


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    deps = parse_deps(puzzle_input)
    finished = []
    available = set()
    s = set()
    for dep in deps:
        [s.add(d) for d in deps[dep] if d not in deps.keys()]
    for v in sorted(s):
        available.add(v)
    while available:
        next = sorted(available)[0]
        available.remove(next)
        finished.append(next)
        for k, v in deps.items():
            if v.issubset(set(finished)):
                available.add(k)
        for a in available:
            if a in deps.keys():
                del deps[a]
    return str(''.join(finished))


def part_b(puzzle_input, workers=5, offset=60):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    deps = parse_deps(puzzle_input)
    finished = []
    queue = []
    processing = []
    t = 0

    def process():
        nonlocal queue
        while len(processing) < workers and queue:
            c = min(queue)
            queue = [e for e in queue if e != c]
            processing.append((string.ascii_uppercase.index(c) + 1 + t + offset, c))

    for dep in deps:
        [queue.append(c) for c in deps[dep] if c not in deps.keys()]
    queue = list(set(queue))
    process()
    while processing or queue:
        for time, next_char in processing:
            if time == t:
                finished.append(next_char)
                processing.remove((time, next_char))
        for dep in set(deps.keys()):
            if deps[dep].issubset(finished):
                queue.append(dep)
                del deps[dep]
        process()
        t += 1
    return str(t - 1)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
