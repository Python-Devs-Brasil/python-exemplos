import unittest

def fun(x):
    return x + 4

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)