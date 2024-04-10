"""
Write Calc test case
"""
from django.test import SimpleTestCase
from app import calc
class TestClass(SimpleTestCase):

    def test_calc(self):
        res = calc.add(2, 3)
        self.assertEqual(res, 6)
