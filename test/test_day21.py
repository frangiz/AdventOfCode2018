"""The tests for day21."""
from days import day21
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    # No examples for part a
    '''@data(
        [],
        [])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day21.part_a(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_a(self): # noqa D102
        result = day21.part_a(helpers.get_file_contents('day21.txt'))
        self.assertEqual(result, '212115')

    # No examples for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day21.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day21.part_b(helpers.get_file_contents('day21.txt'))
        self.assertEqual(result, '')
