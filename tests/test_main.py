import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io


class MyTestCase(unittest.TestCase):
    def test_step1(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
