import unittest

import hw4_fin as hw4

from unittest.mock import patch
from io import StringIO
from random import randint, sample


class TestHw4(unittest.TestCase):
    def test_fv(self):
        PV = randint(100_000, 300_000)

        # calculating a percentage from 3.0 to 5.0
        r = randint(300, 500) / 10_000

        n = sample([15, 30], 1)[0]

        user_inputs = [PV, r, n]

        with patch('builtins.input', side_effect=user_inputs), patch('sys.stdout', new=StringIO()) as std_out:
            hw4.fv()
            expected_val = PV * (1 + r) ** n
            expected_val_str = str(expected_val).split('.')[0]
            self.assertIn(expected_val_str, std_out.getvalue())

    def test_pv(self):
        FV = randint(100_000, 300_000)

        # calculating a percentage from 3.0 to 5.0
        r = randint(300, 500) / 10_000

        n = sample([15, 30], 1)[0]

        user_inputs = [FV, r, n]

        with patch('builtins.input', side_effect=user_inputs), patch('sys.stdout', new=StringIO()) as std_out:
            hw4.pv()
            expected_val = FV / ((1 + r) ** n)
            expected_val_str = str(expected_val).split('.')[0]
            self.assertIn(expected_val_str, std_out.getvalue())

    def test_pmt(self):
        PV = randint(100_000, 300_000)

        # calculating a percentage from 3.0 to 5.0
        r = randint(300, 500) / 10_000

        n = sample([15, 30], 1)[0]

        user_inputs = [PV, r, n]

        with patch('builtins.input', side_effect=user_inputs), patch('sys.stdout', new=StringIO()) as std_out:
            hw4.pmt(PV, r, n)
            expected_val = (r * PV) / (1 - (1 + r) ** -n)
            expected_val_str = str(expected_val).split('.')[0]
            self.assertIn(expected_val_str, std_out.getvalue())
