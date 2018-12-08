"""--- Day 08: Memory Maneuver ---"""
import helpers


class Node:
    def __init__(self):
        self.children = []
        self.meta = []

    def add_child(self, child):
        self.children.append(child)

    def add_meta(self, meta):
        self.meta.append(meta)

    def sum_meta(self):
        return sum(self.meta + [s.sum_meta() for s in self.children])

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.meta)
        else:
            val = 0
            for i in self.meta:
                if i != 0 and i <= len(self.children):
                    val += self.children[i - 1].get_value()
            return val

    def __repr__(self):
        return 'meta: {}, value: {}'.format(self.meta, self.get_value())


def draw_tree(node, indent=0):
    print(('  ' * indent) + str(node))
    for child in node.children:
        draw_tree(child, indent + 1)


def parse(data):
    nbr_children, nbr_meta = data[:2]
    data = data[2:]
    node = Node()

    for _ in range(nbr_children):
        child, data = parse(data)
        node.add_child(child)
    for i in range(nbr_meta):
        node.add_meta(data[i])
    return (node, data[nbr_meta:])


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    data = helpers.to_ints((''.join(puzzle_input)).split())
    root, _ = parse(data)
    return str(root.sum_meta())


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    data = helpers.to_ints((''.join(puzzle_input)).split())
    root, _ = parse(data)
    return str(root.get_value())


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
