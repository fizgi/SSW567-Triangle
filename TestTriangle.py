""" The primary goal of this file is to demonstrate a simple unittest implementation

    author: Fatih Izgi
    date: 16-Feb-2021
    python: v3.9.1
"""

import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    """ Test class of the methods """

    # Right triangle tests

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5, 13, 12), 'Right', '5,13,12 is a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(12, 5, 13), 'Right', '12,5,13 is a Right triangle')

    # Equilateral triangle tests

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')

    # Isosceles triangle tests

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,4 should be Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3, 5, 3), 'Isosceles', '3,5,3 should be Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles', '4,6,6 should be Isosceles')

    # Scalene triangle tests

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(6, 5, 4), 'Scalene', '6,5,4 should be Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(5, 4, 6), 'Scalene', '5,4,6 should be Scalene')

    def testScaleneTriangleD(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be Scalene')

    # Not a triangle tests

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(4, 7, 21), 'NotATriangle', '4,7,21 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle', '5, 1, 1 is not a triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(2, 6, 2), 'NotATriangle', '2,6,2 is not a triangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(1, 1, 5), 'NotATriangle', '1,1,5 is not a triangle')

    # Invalid input tests

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-4, -6, -7), 'InvalidInput', '-4,-6,-7 InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput', '201,201,201 InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(150, 150, 250), 'InvalidInput', '150,150,200 InvalidInput')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle('x', 'y', 'z'), 'InvalidInput', 'x, y, z InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
