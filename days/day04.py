"""--- Day 04: Repose Record ---"""
from datetime import datetime, timedelta
from collections import defaultdict
from collections import Counter


def parse(puzzle_input):
    result = []
    for line in sorted(puzzle_input):
        ts_len = len('[YYYY-MM-dd hh:mm]')
        ts = datetime.strptime(line[1:ts_len - 1], '%Y-%m-%d %H:%M')
        action = line[ts_len + 1:]
        result.append((ts, action))
    return result


# ts1 -> start, ts2 -> end
def get_mins(ts1, ts2):
    result = []
    while ts1 < ts2:
        result.append(ts1.minute)
        ts1 = ts1 + timedelta(0, 60)
    return result


def get_sleeps_mins_for_guards(puzzle_input):
    guards_sleep_mins = defaultdict(list)
    start_to_sleep = None
    current_guard_id = 0
    for ts, action in parse(puzzle_input):
        if action.startswith('Guard'):
            current_guard_id = int(action.split()[1][1:])
        elif action.startswith('falls asleep'):
            start_to_sleep = ts
        elif action.startswith('wakes up'):
            guards_sleep_mins[current_guard_id].extend(get_mins(start_to_sleep, ts))
    return guards_sleep_mins


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    guards_sleep_mins = get_sleeps_mins_for_guards(puzzle_input)
    guard = max(guards_sleep_mins.items(), key=lambda pair: len(pair[1]))[0]
    max_min = Counter(guards_sleep_mins[guard]).most_common(1)[0][0]
    return str(guard * int(max_min))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    guards_sleep_mins = get_sleeps_mins_for_guards(puzzle_input)
    guard = 0
    max_mins = 0
    count = 0
    for k, v in guards_sleep_mins.items():
        max_min, occurences = Counter(v).most_common(1)[0]
        if occurences > count:
            guard = k
            max_mins = max_min
            count = occurences
    return str(guard * max_mins)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
