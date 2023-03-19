"""
Peter Demachkie
pdemachk@uscs.edu
https://github.com/PeterDemachkie/LinkedList
ListTest.py
"""

from LinkedList import List
import unittest

# ListTest Module: runs unit tests to determine whether the List ADT functions as designed

class ListTest(unittest.TestCase):

    def test_getFront1(self):
        L = List()
        L.prepend(5)
        self.assertEqual(5, L.getFront())

    def test_getFront2(self):
        L = List()
        L.append(1)
        L.append(2)
        L.append(3)
        L.prepend(4)
        L.prepend(5)
        self.assertEqual(5, L.getFront())

    def test_getFront3(self):
        L = List()
        L.append(1)

if __name__ == '__main__':
    unittest.main()