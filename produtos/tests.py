from django.test import TestCase

class SimpleTest(TestCase):
    # Teste de adição simples
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    # Teste de subtração simples
    def test_basic_subtraction(self):
        self.assertEqual(5 - 2, 3)

    # Teste de multiplicação simples
    def test_basic_multiplication(self):
        self.assertEqual(3 * 3, 9)

    # Teste de divisão simples
    def test_basic_division(self):
        self.assertEqual(8 / 2, 4)
