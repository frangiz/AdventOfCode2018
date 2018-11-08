import argparse
import unittest
from test.time_logging_test_runner import TimeLoggingTestRunner

tests_abbreviations = {
    'ea': 'test_example_a',
    'aa': 'test_answer_part_a',
    'eb': 'test_example_b',
    'ab': 'test_answer_part_b'}


def run_tests(prefix='test', pattern='test*.py', verbose=False):
    verbosity_level = 2 if verbose else 1
    loader = unittest.TestLoader()
    loader.testMethodPrefix = prefix
    tests = loader.discover('test', pattern)
    runner = TimeLoggingTestRunner(verbosity=verbosity_level)
    runner.run(tests)


def main():
    parser = argparse.ArgumentParser(prog='AdventOfCode2018')
    parser.add_argument('-a', '--all', action='store_true', help='Will run all the tests')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-d', '--day', type=str, help='The day to test.')
    parser.add_argument('-t', '--tests', choices=tests_abbreviations.keys(),
                        help='Which tests to run: ' + str(tests_abbreviations))

    args = parser.parse_args()

    if args.all:
        run_tests(verbose=args.verbose)
    elif args.day is not None:
        file_pattern = 'test_day' + args.day + '.py'
        if args.tests is not None:
            prefix = tests_abbreviations[args.tests]
            run_tests(prefix=prefix, pattern=file_pattern, verbose=args.verbose)
        else:
            run_tests(pattern=file_pattern, verbose=args.verbose)
    else:
        run_tests(verbose=args.verbose)


if __name__ == '__main__':
    main()
