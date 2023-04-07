"""
An example test case with unittest.
See: https://docs.python.org/3/library/unittest.html
"""
import unittest
from rpa.amazon.amazon_rpa import AmazonScript

class TestCookie(unittest.TestCase):

    def test_upper(self):
        as_var = AmazonScript()
        self.assertEqual(as_var.val, 'hello1')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)