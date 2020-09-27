import unittest
import sys

from io import StringIO

import hw1

class TestHomework1(unittest.TestCase):

    def test_greeting(self):
        # Setup capturing the console output
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        # call the function
        hw1.greeting()

        # Reset things back to normal
        sys.stdout = sys.__stdout__

        # check that proper changes were made
        self.assertIn("Hello", capturedOutput.getvalue())
        self.assertNotIn("KronosKoders", capturedOutput.getvalue())
