import unittest

def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
    

class TestFibonacci(unittest.TestCase):
    
    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado,0)
    
    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado,1)

    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado,1)

    def test_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    def test_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado,3)

    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado,5)

    def test_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado,8)
    
    def test_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado,13)
    
    def test_8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado,21)

    def test_15(self):
        resultado = fibonacci(15)
        self.assertEqual(resultado,610)


unittest.main()
