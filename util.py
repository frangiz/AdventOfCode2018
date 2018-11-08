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


def get_adjecent(pos):
    '''
    Returns all adjacent Points of pos.
    '''
    return [
            Point(pos[0] + 1, pos[1]),
            Point(pos[0] + 1, pos[1] - 1),
            Point(pos[0], pos[1] - 1),
            Point(pos[0] - 1, pos[1] - 1),
            Point(pos[0] - 1, pos[1]),
            Point(pos[0] - 1, pos[1] + 1),
            Point(pos[0], pos[1] + 1),
            Point(pos[0] + 1, pos[1] + 1)
            ]
