import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    """Testing Class"""
    def test_circuit(self):
        """Test circuit function"""
        solution = Solution()
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(solution.canCompleteCircuit(gas, cost), 3)
        gas = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(solution.canCompleteCircuit(gas, cost), -1)

if __name__ == '__main__':
    unittest.main()