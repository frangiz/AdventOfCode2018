"""The tests for day22."""
from days import day22
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['depth: 510', 'target: 10,10'], '114'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day22.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day22.part_a(helpers.get_file_contents('day22.txt'))
        self.assertEqual(result, '11972')

    @data(
        [['depth: 510', 'target: 10,10'], '45'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day22.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day22.part_b(helpers.get_file_contents('day22.txt'))
        self.assertEqual(result, '1092')
