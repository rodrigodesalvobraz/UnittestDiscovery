import unittest

from ..util.foo import run_foo


class TestSomeIntegration(unittest.TestCase):
    def test_some_integration(self):
        run_foo()
        print("Integration package")
        assert True
