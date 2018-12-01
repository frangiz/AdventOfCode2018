"""Generates the files needed for the next day."""
import os
import re
import urllib.request

day_template = '''\"\"\"--- Day {0}: {1} ---\"\"\"
import helpers


def part_a(puzzle_input):
    \"\"\"
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    \"\"\"
    return str(0)


def part_b(puzzle_input):
    \"\"\"
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    \"\"\"
    return str(0)


def solve(puzzle_input):
    \"\"\"Returs the answer for both parts.\"\"\"
    return {{'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}}
'''

test_day_template = '''\"\"\"The tests for day{0}.\"\"\"
from days import day{0}
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
        result = day{0}.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day{0}.part_a(helpers.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')

    @data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day{0}.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day{0}.part_b(helpers.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')
'''

readme_line_template = '\n|[Day {2}: {1}](http://adventofcode.com/2018/day/{2}) | [day{0}.py](days/day{0}.py) | --- |'


def regenerate_days_init_file(number_of_days):
    """
    Renegerates the __init__.py file in the module days.

    The method have some logic to indent the list when it gets close to the
    80 charactes wide mark.

    Args:
        number_of_days (int): The number of days to be written to the file.
    """
    days = ['\"day{num:02d}\"'.format(num=day) for day in range(1, number_of_days + 1)]
    text = '__all__ = [ {list_of_days} ] # noqa D104'.format(list_of_days=', '.join(days[:7]))
    new_line_with_prefix = '\n' + ' ' * 12
    if len(days) > 7:
        text = text.replace(' ]', ',')
        for i, day in enumerate(days[7:]):
            if i % 7 == 0:
                text += new_line_with_prefix
            text += day + ', '
        text = text[:-2] + ' ]'

    with open('days/__init__.py', 'w') as f:
        f.write(text)
        f.write('\n')


def create_files(day, dayname):
    """
    Create the files needed for a new day.

    Each day needs three files.
        - days/day[n].py - The source code for the day.
        - test/test_day[n].py - The corresponding tests.
        - input/day[n].txt - The input formatted as the input from the website.
    Each day will also be appended to the __init__.py file for the module days.

    Args:
        day (string): The day to create formatted with two or more digits.
        dayname (string): The name of the day.

    """
    if not os.path.isfile('days/day' + day + '.py'):
        with open('days/day' + day + '.py', 'w') as f:
            f.writelines(day_template.format(day, dayname))
    if not os.path.isfile('test/test_day' + day + '.py'):
        with open('test/test_day' + day + '.py', 'w') as f:
            f.writelines(test_day_template.format(day))
    if not os.path.isfile('inputs/day' + day + '.txt'):
        with open('inputs/day' + day + '.txt', 'w') as f:
            pass
    if os.path.isfile('README.md'):
        with open('README.md', 'a') as f:
            f.write(readme_line_template.format(day, dayname, int(day)))
    regenerate_days_init_file(int(day))


def get_dayname(day):
    """
    Fetch the day from the AoC website and parses the name.

    Args:
        day (int): The day to fetch the name for.
    Returns:
        string: The name for the day.

    """
    try:
        contents = urllib.request.urlopen("http://adventofcode.com/2018/day/{0}".format(day)).read()
        m = re.search('<article class=\"day-desc\">.*<h2>.*: (.*) ---</h2>', str(contents))
        if m is not None:
            return m.group(1)
    except urllib.error.HTTPError:
        return 'n/a'
    return 'n/a'


def day_to_gen():
    """
    Return the day to generate in the inverval [1-25].

    Returns:
        string/None: A string formatted with two digits if the day is valid else None.

    """
    files = len(os.listdir('inputs'))
    if files <= 24:  # 25 puzzle days for AoC
        return '{0:02d}'.format(files + 1)
    else:
        return None


def main(): # noqa D103
    day = day_to_gen()
    if day is not None:
        dayname = get_dayname(int(day))
        create_files(day, dayname)
    else:
        print('Max number of days created.')


if __name__ == '__main__':
    main()
