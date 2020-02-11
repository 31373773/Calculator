import unittest

from MathOperations.addition import Addition
from MathOperations.divide import Division
from MathOperations.logarithm import Logarithm
from MathOperations.multiply import Multiplication
from MathOperations.square import Exponentiation
from MathOperations.root import Root
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_divide(self):
        self.assertEqual(3, Division.divide(12, 4))

    def test_MathOperations_multiply(self):
        self.assertEqual(50, Multiplication.mult(5, 10))

    def test_MathOperations_square(self):
        self.assertEqual(16, Exponentiation.sqr(4, 2))

    def test_MathOperations_root(self):
        self.assertEqual(10, Root.nRoot(2, 100))

    def test_MathOperations_logarithm(self):
        self.assertEqual(3, Logarithm.log(8, 2))


if __name__ == '__main__':
    unittest.main()
