import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_return_divide(self):
        result = self.calculator.divide(12, 4)
        self.assertEqual(3, result)

    def test_calculator_access_divide_result(self):
        self.calculator.divide(12, 4)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_logarithm(self):
        result = self.calculator.logarithm(8, 2)
        self.assertEqual(3, result)

    def test_calculator_access_logarithm_result(self):
        self.calculator.logarithm(8, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_multiply(self):
        result = self.calculator.multiply(5, 10)
        self.assertEqual(50, result)

    def test_calculator_access_multiply_result(self):
        self.calculator.multiply(5, 10)
        self.assertEqual(50, self.calculator.Result)

    def test_calculator_return_root(self):
        result = self.calculator.root(2, 100)
        self.assertEqual(10, result)

    def test_calculator_access_root_result(self):
        self.calculator.root(2, 100)
        self.assertEqual(10, self.calculator.Result)

    def test_calculator_return_square(self):
        result = self.calculator.square(4, 2)
        self.assertEqual(16, result)

    def test_calculator_access_square_result(self):
        self.calculator.square(4, 2)
        self.assertEqual(16, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
