import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calc.substract(4, 2)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()