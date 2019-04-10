import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertNotEqual(repr(Location("Narnia", 1, 2)), repr(loc))
        self.assertEqual(repr(Location("Candyland", 0, 4)), repr(Location("Candyland", 0, 4)))
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(Location("SLO", 35.3, -120.7), Location("SLO", 35.3, -120.7))
        self.assertEqual(loc, Location("SLO", 35.3, -120.7))
        self.assertNotEqual(Location("Candyland", 0, 4), Location("America", 0, 4))
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
