"""The tests for day08."""
from days import day08
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'], '138'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day08.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day08.part_a(helpers.get_file_contents('day08.txt'))
        self.assertEqual(result, '46829')

    @data(
        [['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'], '66'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day08.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day08.part_b(helpers.get_file_contents('day08.txt'))
        self.assertEqual(result, '37450')
