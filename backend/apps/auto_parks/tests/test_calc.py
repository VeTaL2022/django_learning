from unittest import TestCase

from ..services import calc


class CalculatorTestCase(TestCase):
    def test_minus(self):
        result = calc(1, 2, '-')
        self.assertEqual(result, -1)

    def test_plus(self):
        result = calc(1, 2, '+')
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = calc(1, 2, '*')
        self.assertEqual(result, 2)
