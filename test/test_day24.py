"""The tests for day24."""
from days import day24
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [],
        [])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day24.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day24.part_a(helpers.get_file_contents('day24.txt'))
        self.assertEqual(result, '')

    @data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day24.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day24.part_b(helpers.get_file_contents('day24.txt'))
        self.assertEqual(result, '')
