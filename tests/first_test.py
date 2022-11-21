import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correctly(self):
        assert self.calc.multiply(self, 8, 2) == 16

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 8, 2) == 10
