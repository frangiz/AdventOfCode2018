"""The tests for day04."""
from days import day04
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['[1518-11-01 00:00] Guard #10 begins shift',
          '[1518-11-01 00:05] falls asleep',
          '[1518-11-01 00:25] wakes up',
          '[1518-11-01 00:30] falls asleep',
          '[1518-11-01 00:55] wakes up',
          '[1518-11-01 23:58] Guard #99 begins shift',
          '[1518-11-02 00:40] falls asleep',
          '[1518-11-02 00:50] wakes up',
          '[1518-11-03 00:05] Guard #10 begins shift',
          '[1518-11-03 00:24] falls asleep',
          '[1518-11-03 00:29] wakes up',
          '[1518-11-04 00:02] Guard #99 begins shift',
          '[1518-11-04 00:36] falls asleep',
          '[1518-11-04 00:46] wakes up',
          '[1518-11-05 00:03] Guard #99 begins shift',
          '[1518-11-05 00:45] falls asleep',
          '[1518-11-05 00:55] wakes up'], '240'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day04.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day04.part_a(helpers.get_file_contents('day04.txt'))
        self.assertEqual(result, '35623')

    @data(
        [['[1518-11-01 00:00] Guard #10 begins shift',
          '[1518-11-01 00:05] falls asleep',
          '[1518-11-01 00:25] wakes up',
          '[1518-11-01 00:30] falls asleep',
          '[1518-11-01 00:55] wakes up',
          '[1518-11-01 23:58] Guard #99 begins shift',
          '[1518-11-02 00:40] falls asleep',
          '[1518-11-02 00:50] wakes up',
          '[1518-11-03 00:05] Guard #10 begins shift',
          '[1518-11-03 00:24] falls asleep',
          '[1518-11-03 00:29] wakes up',
          '[1518-11-04 00:02] Guard #99 begins shift',
          '[1518-11-04 00:36] falls asleep',
          '[1518-11-04 00:46] wakes up',
          '[1518-11-05 00:03] Guard #99 begins shift',
          '[1518-11-05 00:45] falls asleep',
          '[1518-11-05 00:55] wakes up'], '4455'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day04.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day04.part_b(helpers.get_file_contents('day04.txt'))
        self.assertEqual(result, '23037')
