import time
from unittest.runner import TextTestResult

class TimeLoggingTestResult(TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_timings = []

    def startTest(self, test):
        self._test_started_at = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        elapsed = time.time() - self._test_started_at
        name = self.getDescription(test)
        self._test_timings.append((name, elapsed))
        super().addSuccess(test)

    def getTestTimings(self):
        return self._test_timings
