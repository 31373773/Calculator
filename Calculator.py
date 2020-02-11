from MathOperations.addition import Addition
from MathOperations.divide import Division
from MathOperations.logarithm import Logarithm
from MathOperations.multiply import Multiplication
from MathOperations.square import Exponentiation
from MathOperations.root import Root
from MathOperations.subtraction import Subtraction


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def divide(self, dividend, divisor):
        self.Result = Division.divide(dividend, divisor)
        return self.Result

    def logarithm(self, variable, base):
        self.Result = Logarithm.log(variable, base)
        return self.Result

    def multiply(self, multiplier, multiplicand):
        self.Result = Multiplication.mult(multiplier, multiplicand)
        return self.Result

    def root(self, degree, radicand):
        self.Result = Root.nRoot(degree, radicand)
        return self.Result

    def square(self, base, exponent):
        self.Result = Exponentiation.sqr(base, exponent)
        return self.Result
