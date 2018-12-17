"""The tests for day16."""
from days import day16
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            'Before: [3, 2, 1, 1]',
            '9 2 1 2',
            'After:  [3, 2, 2, 1]'], '1'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day16.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day16.part_a(helpers.get_file_contents('day16.txt'))
        self.assertEqual(result, '521')

    # No example for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day16.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day16.part_b(helpers.get_file_contents('day16.txt'))
        self.assertEqual(result, '594')
