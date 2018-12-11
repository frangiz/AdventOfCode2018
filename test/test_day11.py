"""The tests for day11."""
from days import day11
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [(3, 5, 8), 4],
        [(122, 79, 57), -5],
        [(217, 196, 39), 0],
        [(101, 153, 71), 4])
    @unpack
    def test_calc_power_level(self, test_input, expected): # noqa D102
        x, y, serial_number = test_input
        result = day11.calc_power_level(x, y, serial_number)
        self.assertEqual(result, expected)

    @data(
        [['18'], '33,45'],
        [['42'], '21,61'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day11.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day11.part_a(helpers.get_file_contents('day11.txt'))
        self.assertEqual(result, '243,43')

    @data(
        [['18'], '90,269,16'],
        [['42'], '232,251,12'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day11.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day11.part_b(helpers.get_file_contents('day11.txt'))
        self.assertEqual(result, '236,151,15')
