import unittest
import calc

class TestCalc(unittest.TestCase):
    """Testing class"""
    #You can add as many test as needed
    def test_add(self):
        """Test add function"""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 2),1)

    def test_subtract(self):
        """Test subtract"""
        self.assertEqual(calc.subtract(4, 2), 2)
        self.assertEqual(calc.subtract(0, -2), 2)
        self.assertNotEqual(calc.subtract(9, 2), 8)
    def test_divide(self):
        """"""
        self.assertRaises(ValueError, calc.divide, 3, 0)

if __name__ == "__main__":
    unittest.main()