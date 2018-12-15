import os
from collections import namedtuple, deque


def get_file_contents(filename):
    inputfilename = os.path.join('inputs', filename)
    contents = []
    with open(inputfilename, 'r') as f:
        for line in f:
            contents.append(line)
    return contents


Point = namedtuple('Point', 'x y')


def get_adjecent_4(pos, valid=lambda point: True):
    '''
    Returns all adjacent Points of pos.
    '''
    neighbours = []
    for p in [Point(pos.x - 1, pos.y), Point(pos.x + 1, pos.y),
              Point(pos.x, pos.y - 1), Point(pos.x, pos.y + 1)]:
        if valid(p):
            neighbours.append(p)
    return neighbours


def get_adjecent_8(pos, valid=lambda point: True):
    '''
    Returns all adjacent Points of pos.
    '''
    neighbours = []
    for x in range(pos.x - 1, pos.x + 2):
        for y in range(pos.y - 1, pos.y + 2):
            p = Point(x, y)
            if valid(p) and ((p > pos) - (p < pos)):
                neighbours.append(p)
    return neighbours


def get_manhattan_dist(pos1, pos2):
    '''
    Calculates the manhattan distance between two points. Calling such
    a simple method increases the overhead and should more be seen as
    a reference implementation or called very infrequently.
    '''
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def clamp(value, min_, max_):
    '''
    Clamp the value so that it is at least min_ and at most max_
    '''

    if value < min_:
        return min_
    if value > max_:
        return max_
    return value


def to_ints(container):
    '''
    Return the given items as ints, in the same container type
    '''

    t = type(container)
    return t(map(int, container))


def shortest_path(start, end, valid_pos=lambda point: True):
    class Node:
        def __init__(self, pos, length, parent):
            self.pos = pos
            self.length = length
            self.parent = parent

        def __repr__(self):
            return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    visited = set()
    unvisited = deque()
    unvisited.append(Node(start, 0, None))
    reached_the_end = False
    solutions = []
    while unvisited:
        node = unvisited.popleft()
        visited.add(node.pos)
        if node.pos == end:
            if len(solutions) == 0:
                solutions.append(node)
                reached_the_end = True
            elif solutions[0].length == node.length:
                solutions.append(node)
        if not reached_the_end:
            for neighbour in get_adjecent_4(node.pos):
                if neighbour not in visited:
                    if neighbour == end:
                        unvisited.append(Node(neighbour, node.length + 1, node))
                    elif valid_pos(neighbour):
                        unvisited.append(Node(neighbour, node.length + 1, node))
    # Convert the nodes that reached the end to a list of points
    result = []
    for node in solutions:
        path = []
        while node.parent is not None:
            path.append(node.pos)
            node = node.parent
        path.append(node.pos)
        path.reverse()
        result.append(path)
    return result
