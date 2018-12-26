"""The tests for day25."""
from days import day25
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            '0,0,0,0',
            '3,0,0,0',
            '0,3,0,0',
            '0,0,3,0',
            '0,0,0,3',
            '0,0,0,6',
            '9,0,0,0',
            '12,0,0,0'], '2'],
        [[
            '-1,2,2,0',
            '0,0,2,-2',
            '0,0,0,-2',
            '-1,2,0,0',
            '-2,-2,-2,2',
            '3,0,2,-1',
            '-1,3,2,2',
            '-1,0,-1,0',
            '0,2,1,-2',
            '3,0,0,0'], '4'],
        [[
            '1,-1,0,1',
            '2,0,-1,0',
            '3,2,-1,0',
            '0,0,3,1',
            '0,0,-1,-1',
            '2,3,-2,0',
            '-2,2,0,0',
            '2,-2,0,-1',
            '1,-1,0,-1',
            '3,2,0,2'], '3'],
        [[
            '1,-1,-1,-2',
            '-2,-2,0,1',
            '0,2,1,3',
            '-2,3,-2,1',
            '0,2,3,-2',
            '-1,-1,1,-2',
            '0,-2,-1,0',
            '-2,2,3,-1',
            '1,2,2,0',
            '-1,-2,0,-2'], '8'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day25.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day25.part_a(helpers.get_file_contents('day25.txt'))
        self.assertEqual(result, '381')

    # No examples for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day25.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day25.part_b(helpers.get_file_contents('day25.txt'))
        self.assertEqual(result, '')
