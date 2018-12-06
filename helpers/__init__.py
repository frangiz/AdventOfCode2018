import os
from collections import namedtuple


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
