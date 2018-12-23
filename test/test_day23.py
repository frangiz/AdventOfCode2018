"""The tests for day23."""
from days import day23
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            'pos=<0,0,0>, r=4',
            'pos=<1,0,0>, r=1',
            'pos=<4,0,0>, r=3',
            'pos=<0,2,0>, r=1',
            'pos=<0,5,0>, r=3',
            'pos=<0,0,3>, r=1',
            'pos=<1,1,1>, r=1',
            'pos=<1,1,2>, r=1',
            'pos=<1,3,1>, r=1'], '7'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day23.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day23.part_a(helpers.get_file_contents('day23.txt'))
        self.assertEqual(result, '297')

    @data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day23.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day23.part_b(helpers.get_file_contents('day23.txt'))
        self.assertEqual(result, '')
