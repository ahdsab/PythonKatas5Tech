import unittest
from io import StringIO
import sys
from katas.do_n_times import do_n_times, say_hello, print_message


class TestDoNTimes(unittest.TestCase):
    def test_say_hello_3_times(self):
        captured_output = StringIO()
        sys.stdout = captured_output  # redirect stdout

        do_n_times(say_hello, 3)

        sys.stdout = sys.__stdout__  # reset redirect

        output = captured_output.getvalue().strip().split('\n')
        expected = ["Hello!"] * 3
        self.assertEqual(output, expected)

    def test_print_message_5_times(self):
        captured_output = StringIO()
        sys.stdout = captured_output 

        do_n_times(print_message, 5)

        sys.stdout = sys.__stdout__ 

        output = captured_output.getvalue().strip().split('\n')
        expected = ["Python is fun!"] * 5
        self.assertEqual(output, expected)
