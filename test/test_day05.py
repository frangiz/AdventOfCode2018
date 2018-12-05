"""The tests for day05."""
from days import day05
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['dabAcCaCBAcCcaDA'], '10'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day05.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day05.part_a(helpers.get_file_contents('day05.txt'))
        self.assertEqual(result, '11118')

    @data(
        [['dabAcCaCBAcCcaDA'], '4'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day05.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day05.part_b(helpers.get_file_contents('day05.txt'))
        self.assertEqual(result, '6948')
