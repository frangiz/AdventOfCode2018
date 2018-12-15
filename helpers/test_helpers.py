import unittest
from helpers import Point, to_ints, shortest_path


class HelperTestCase(unittest.TestCase):

    def test_to_ints(self):
        my_ints = ['1', '56', '-4']
        converted_ints = to_ints(my_ints)
        self.assertEqual(type(my_ints), type(converted_ints))
        self.assertEqual([1, 56, -4], converted_ints)

    def test_shortest_path_go_right(self):
        paths = shortest_path(Point(1, 1), Point(4, 1))
        self.assertEqual(len(paths), 1)
        self.assertEqual(paths[0], [Point(1, 1), Point(2, 1), Point(3, 1), Point(4, 1)])

    def test_shortest_path_diagonal(self):
        paths = shortest_path(Point(0, 0), Point(2, 1))
        self.assertEqual(len(paths), 3)
        path1 = [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)]
        path2 = [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)]
        path3 = [Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1)]
        self.assertTrue(path1 in paths)
        self.assertTrue(path2 in paths)
        self.assertTrue(path3 in paths)

    def test_shortest_path_with_blocking_function(self):
        def check_pos(pos):
            if pos.x == 1 and pos.y == 1:
                return False
            return True

        paths = shortest_path(Point(0, 0), Point(2, 1), check_pos)
        self.assertEqual(len(paths), 1)
        path = [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)]
        self.assertTrue(path in paths)

    def test_shortest_path_with_blocking_function2(self):
        def check_pos(pos):
            if (pos.x == 4 and pos.y == 4) or (pos.x == 4 and pos.y == 3):
                return False
            return True

        paths = shortest_path(Point(3, 4), Point(4, 2), check_pos)
        self.assertEqual(len(paths), 1)
        path = [Point(3, 4), Point(3, 3), Point(3, 2), Point(4, 2)]
        self.assertTrue(path in paths)
