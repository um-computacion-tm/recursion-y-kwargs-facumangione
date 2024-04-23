from sumatoria import sumatoria
import unittest

class TestSumatoria(unittest.TestCase):
    def test_con_1(self):
        resultado = sumatoria(1)
        self.assertEqual(resultado, 1)

    def test_con_2(self):
        resultado = sumatoria(2)
        self.assertEqual(resultado, 3)

    def test_con_3(self):
        resultado = sumatoria(3)
        self.assertEqual(resultado, 6)

    def test_con_4(self):
        resultado = sumatoria(4)
        self.assertEqual(resultado, 10)

    def test_con_5(self):
        resultado = sumatoria(5)
        self.assertEqual(resultado, 15)

    def test_con_6(self):
        resultado = sumatoria(6)
        self.assertEqual(resultado, 21)

unittest.main()