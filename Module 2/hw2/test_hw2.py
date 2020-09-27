import unittest

from unittest.mock import patch
from io import StringIO
from random import randint, sample

from hw2_welcome import welcome
from hw2_rate import rate
from hw2_temp import temp

class TestHw2(unittest.TestCase):

    def test_welcome(self):
        usernames = ("KronosKoders", "Kronos", "Caladin", "Shadesmare", "Anakin", "Bulbasaur")
        user_input = sample(usernames, 1)
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            welcome()
            self.assertIn(user_input[0], std_out.getvalue())
            self.assertIn('Welcome', std_out.getvalue())

    def test_rate(self):
        user_input = (randint(34, 42), randint(1800, 2600) / 100)
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            rate()
            expected_value = user_input[0] * user_input[1]
            whole, mantissa = str(expected_value).split('.')
            expected_value_str = '.'.join((whole, mantissa[:2]))
            self.assertIn(expected_value_str, std_out.getvalue())

    def test_temp(self):
        user_input = (randint(20, 34),)
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            temp()
            expected_value = user_input[0] * 1.8 + 32
            whole, mantissa = str(expected_value).split('.')
            expected_value_str = '.'.join((whole, mantissa[:2]))
            self.assertIn(expected_value_str, std_out.getvalue())
