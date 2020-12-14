import unittest

from unittest.mock import patch
from io import StringIO
from random import sample, randint

from hw3_str_len import str_len
from hw3_str_assemble import str_assemble
from hw3_str_replace import str_replace

class TestHw3(unittest.TestCase):
    def test_str_len(self):
        # NOTE: If you're reading this test case and can correctly identify
        # where each statement below comes from and give me those sources, I'll
        # give you extra credit. ;)  There may be other hints found in other
        # tests as well.
        statements = (
            "This is the way",
            "Po Ta Toes! Boil em, mash em, stick em in a stew!",
            "Shut up baby I know it!",
            "Ah, the outdoors, I visited that mythical place once"
        )
        user_input = sample(statements, 1)
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            str_len()
            expected = str(len(user_input[0]))
            self.assertIn(expected, std_out.getvalue())

    def test_str_concat(self):
        dates = (
            "10-30-2020 0630",
            "12-18-2002 0830",
            "01-01-3000 0000",
            "08-31-2010 0239"
        )
        statuses = (
            "Child",
            "Sam",
            "slurm",
            "Oathbringer"
        )
        messages = (
            "This is the way",
            "Po Ta Toes! Boil em, mash em, stick em in a stew!",
            "Shut up baby I know it!",
            "Ah, the outdoors, I visited that mythical place once"
        )

        index = randint(0, 3)
        user_input = (dates[index], statuses[index], messages[index])
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            str_assemble()
            expected = f"[{user_input[0]}]: ({user_input[1]}) {user_input[2]}"
            self.assertIn(expected, std_out.getvalue())

    def test_str_replace(self):
        inputs = (
            ("This is the way", "is", "was"),
            ("Po Ta Toes! Boil em, mash em, stick em in a stew!", "em", "them"),
            ("Shut up baby I know it!", "Shut up", "Shut it"),
            ("Ah, the outdoors, I visited that mythical place once", "mythical", "mystical")
        )

        user_input = sample(inputs, 1)[0]
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as std_out:
            str_replace()
            self.assertIn(user_input[0].replace(user_input[1], user_input[2]), std_out.getvalue())
