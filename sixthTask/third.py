import unittest
import sys
import time

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_overflow(self):
        with self.assertRaises(ValueError):
            factorial(100000)

    def test_factorial_large_number(self):
        self.assertTrue(factorial(20) > 0)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

def run_tests():
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFactorial)
    test_runner = unittest.TextTestRunner()
    start_time = time.time()
    test_runner.run(test_suite)
    end_time = time.time()
    print(f"Время выполнения тестов: {end_time - start_time} секунд")

if __name__ == "__main__":
    run_tests()
