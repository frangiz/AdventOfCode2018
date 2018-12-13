"""The tests for day13."""
from days import day13
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['|', 'v', '|', '|', '|', '^', '|'], '0,3'],
        [[
            '/->-\\        ',
            '|   |  /----\\',
            '| /-+--+-\\  |',
            '| | |  | v  |',
            '\\-+-/  \\-+--/',
            '  \\------/   '], '7,3'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day13.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day13.part_a(helpers.get_file_contents('day13.txt'))
        self.assertEqual(result, '100,21')

    @data(
        [[
            '/>-<\\  ',
            '|   |  ',
            '| /<+-\\',
            '| | | v',
            '\\>+</ |',
            '  |   ^',
            '  \\<->/'], '6,4'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day13.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day13.part_b(helpers.get_file_contents('day13.txt'))
        self.assertEqual(result, '113,109')
