import unittest
import time
from katas.time_me import measure_execution_time, sample_function, quick_function


class TestMeasureExecutionTime(unittest.TestCase):
    def test_sample_function_time(self):
        time_taken = measure_execution_time(sample_function)
        self.assertGreaterEqual(time_taken, 0.5)
        self.assertLess(time_taken, 0.6)  # Allowing a small margin

    def test_quick_function_time(self):
        time_taken = measure_execution_time(quick_function)
        # quick_function should be very fast, under 0.1 second
        self.assertLess(time_taken, 0.1)