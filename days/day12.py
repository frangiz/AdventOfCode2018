"""--- Day 12: Subterranean Sustainability ---"""


def count_plants(zero_pointer, plants):
    return sum(i - zero_pointer for i, c in enumerate(plants) if c == '#')


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    state = puzzle_input[0].replace('initial state: ', '').strip()
    rules = {}
    for line in puzzle_input[2:]:
        trigger, result = line.strip().split(' => ')
        rules[trigger] = result
    zero_pointer = 0
    for _ in range(20):
        zero_pointer += 2
        state = '....' + state + '....'
        tmp_state = ''
        for i in range(2, len(state) - 2):
            sub_pots = state[i - 2:i + 3]
            if sub_pots in rules:
                pot = rules[sub_pots]
            else:
                pot = '.'
            tmp_state += pot
        if tmp_state.startswith('..'):
            tmp_state = tmp_state[2:]
            zero_pointer -= 2
        if tmp_state.endswith('..'):
            tmp_state = tmp_state[:-2]
        state = tmp_state
    return str(count_plants(zero_pointer, state))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    state = puzzle_input[0].replace('initial state: ', '').strip()
    rules = {}
    for line in puzzle_input[2:]:
        trigger, result = line.strip().split(' => ')
        rules[trigger] = result
    zero_pointer = 0
    last_sum = count_plants(zero_pointer, state)
    last_deltas = []
    for gen in range(50_000_000_000):
        zero_pointer += 2
        state = '....' + state + '....'
        tmp_state = ''
        for i in range(2, len(state) - 2):
            sub_pots = state[i - 2:i + 3]
            if sub_pots in rules:
                pot = rules[sub_pots]
            else:
                pot = '.'
            tmp_state += pot
        while tmp_state[0] == '.':
            tmp_state = tmp_state[1:]
            zero_pointer -= 1
        while tmp_state[-1] == '.':
            tmp_state = tmp_state[:-1]
        state = tmp_state
        new_sum = count_plants(zero_pointer, state)
        new_delta = new_sum - last_sum
        last_sum = new_sum
        last_deltas.append(new_delta)
        len_deltas = len(last_deltas)
        if len_deltas > 1000 and sum(last_deltas) // len_deltas == new_delta:
            return str((50_000_000_000 - gen - 1) * new_delta + last_sum)
        if len_deltas > 1000:
            last_deltas.pop(0)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
