import unittest
from test.time_logging_test_result import TimeLoggingTestResult


class TimeLoggingTestRunner(unittest.TextTestRunner):
    def __init__(self, slow_test_threshold=0.3, *args, **kwargs):
        self.slow_test_threshold = slow_test_threshold
        super().__init__(
            resultclass=TimeLoggingTestResult,
            *args,
            **kwargs)

    def run(self, test):
        result = super().run(test)

        self.stream.writeln("\nSlow Tests (>{0:.03}s):".format(self.slow_test_threshold))

        got_a_slow_test = False
        for name, elapsed in result.getTestTimings():
            if elapsed > self.slow_test_threshold:
                got_a_slow_test = True
                self.stream.writeln("({0:.3f}s) {1}".format(elapsed, name))
        if not got_a_slow_test:
            self.stream.writeln("-- None --")
        return result
