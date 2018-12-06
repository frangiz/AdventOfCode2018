"""The tests for day06."""
from days import day06
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9'], '17'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day06.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day06.part_a(helpers.get_file_contents('day06.txt'))
        self.assertEqual(result, '2906')

    @data(
        [['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9'], '16'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day06.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day06.part_b(helpers.get_file_contents('day06.txt'))
        self.assertEqual(result, '50530')
