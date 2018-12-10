"""The tests for day10."""
from days import day10
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            'position=< 9,  1> velocity=< 0,  2>',
            'position=< 7,  0> velocity=<-1,  0>',
            'position=< 3, -2> velocity=<-1,  1>',
            'position=< 6, 10> velocity=<-2, -1>',
            'position=< 2, -4> velocity=< 2,  2>',
            'position=<-6, 10> velocity=< 2, -2>',
            'position=< 1,  8> velocity=< 1, -1>',
            'position=< 1,  7> velocity=< 1,  0>',
            'position=<-3, 11> velocity=< 1, -2>',
            'position=< 7,  6> velocity=<-1, -1>',
            'position=<-2,  3> velocity=< 1,  0>',
            'position=<-4,  3> velocity=< 2,  0>',
            'position=<10, -3> velocity=<-1,  1>',
            'position=< 5, 11> velocity=< 1, -2>',
            'position=< 4,  7> velocity=< 0, -1>',
            'position=< 8, -2> velocity=< 0,  1>',
            'position=<15,  0> velocity=<-2,  0>',
            'position=< 1,  6> velocity=< 1,  0>',
            'position=< 8,  9> velocity=< 0, -1>',
            'position=< 3,  3> velocity=<-1,  1>',
            'position=< 0,  5> velocity=< 0, -1>',
            'position=<-2,  2> velocity=< 2,  0>',
            'position=< 5, -2> velocity=< 1,  2>',
            'position=< 1,  4> velocity=< 2,  1>',
            'position=<-2,  7> velocity=< 2, -2>',
            'position=< 3,  6> velocity=<-1, -1>',
            'position=< 5,  0> velocity=< 1,  0>',
            'position=<-6,  0> velocity=< 2,  0>',
            'position=< 5,  9> velocity=< 1, -2>',
            'position=<14,  7> velocity=<-2,  0>',
            'position=<-3,  6> velocity=< 2, -1>'], ''])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day10.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day10.part_a(helpers.get_file_contents('day10.txt'))
        self.assertEqual(result, 'ZAEZRLZG')

    @data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day10.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day10.part_b(helpers.get_file_contents('day10.txt'))
        self.assertEqual(result, '10105')
