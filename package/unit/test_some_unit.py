import unittest

from ..util.foo import run_foo


class TestSomeUnit(unittest.TestCase):
    def test_some_unit(self):
        run_foo()
        print("Unit package")
        assert True
