import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([11, 2, 4, 16, 3, 0]), 16)
        self.assertEqual(max_list_iter([1, 1, 1, 1, 1]), 1)

    def test_reverse_rec(self):
        with self.assertRaises(ValueError):
            reverse_rec(None)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1]),[1])
        self.assertEqual(reverse_rec([]),[])
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8,9,0]),[0,9,8,7,6,5,4,3,2,1])
    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7)
        #not in list
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None)
        #too high / too low
        self.assertEqual(bin_search(60, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(-6, 0, len(list_val)-1, list_val), None)

        #using different list
        list_val = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), 8)



if __name__ == "__main__":
        unittest.main()

    
