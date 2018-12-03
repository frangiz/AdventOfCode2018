"""The tests for day03."""
from days import day03
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], '4'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day03.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day03.part_a(helpers.get_file_contents('day03.txt'))
        self.assertEqual(result, '98005')

    @data(
        [['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], '3'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day03.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day03.part_b(helpers.get_file_contents('day03.txt'))
        self.assertEqual(result, '331')
