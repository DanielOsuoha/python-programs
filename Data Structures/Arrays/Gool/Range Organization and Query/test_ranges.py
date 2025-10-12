import unittest
from code import ManageRanges

class TestManageRanges(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh ManageRanges instance for each test."""
        self.ranges = ManageRanges()
    
    def test_init(self):
        """Test that ManageRanges initializes correctly."""
        self.assertEqual(len(self.ranges.ranges), 0)
    
    def test_add_single_range(self):
        """Test adding a single range."""
        self.ranges.add(5, 10)
        self.assertEqual(len(self.ranges.ranges), 1)
        self.assertIn((5, 10), self.ranges.ranges)
    
    def test_add_multiple_ranges(self):
        """Test adding multiple non-overlapping ranges."""
        self.ranges.add(5, 10)
        self.ranges.add(15, 20)
        self.ranges.add(25, 30)
        
        self.assertEqual(len(self.ranges.ranges), 3)
        self.assertIn((5, 10), self.ranges.ranges)
        self.assertIn((15, 20), self.ranges.ranges)
        self.assertIn((25, 30), self.ranges.ranges)
    
    def test_find_point_in_range(self):
        """Test finding points within ranges."""
        self.ranges.add(5, 10)
        self.ranges.add(15, 20)
        
        # Test points within ranges
        self.assertTrue(self.ranges.find_point(5))   # Start boundary
        self.assertTrue(self.ranges.find_point(7))   # Middle
        self.assertTrue(self.ranges.find_point(10))  # End boundary
        self.assertTrue(self.ranges.find_point(15))  # Start of second range
        self.assertTrue(self.ranges.find_point(18))  # Middle of second range
        self.assertTrue(self.ranges.find_point(20))  # End of second range
    
    def test_find_point_not_in_range(self):
        """Test finding points outside ranges."""
        self.ranges.add(5, 10)
        self.ranges.add(15, 20)
        
        # Test points outside ranges
        self.assertFalse(self.ranges.find_point(3))   # Before first range
        self.assertFalse(self.ranges.find_point(12))  # Between ranges
        self.assertFalse(self.ranges.find_point(25))  # After last range
    
    def test_find_point_empty_ranges(self):
        """Test finding points when no ranges exist."""
        self.assertFalse(self.ranges.find_point(5))
        self.assertFalse(self.ranges.find_point(0))
        self.assertFalse(self.ranges.find_point(-10))
    
    def test_single_point_range(self):
        """Test ranges with single points."""
        self.ranges.add(5, 5)  # Single point range
        
        self.assertTrue(self.ranges.find_point(5))
        self.assertFalse(self.ranges.find_point(4))
        self.assertFalse(self.ranges.find_point(6))
    
    def test_negative_ranges(self):
        """Test ranges with negative numbers."""
        self.ranges.add(-10, -5)
        self.ranges.add(-2, 3)
        
        self.assertTrue(self.ranges.find_point(-7))   # In negative range
        self.assertTrue(self.ranges.find_point(0))    # In mixed range
        self.assertFalse(self.ranges.find_point(-15)) # Before negative range
        self.assertFalse(self.ranges.find_point(5))   # After positive range
    
    def test_large_ranges(self):
        """Test with large numbers (within constraints)."""
        self.ranges.add(1000000, 2000000)
        
        self.assertTrue(self.ranges.find_point(1500000))
        self.assertFalse(self.ranges.find_point(500000))
        self.assertFalse(self.ranges.find_point(2500000))
    
    def test_overlapping_ranges_current_behavior(self):
        """Test current behavior with overlapping ranges (should be fixed)."""
        self.ranges.add(5, 10)
        self.ranges.add(8, 15)  # Overlaps with first range
        
        # Current implementation will have both ranges
        # This test documents current behavior - should be changed when merging is implemented
        self.assertEqual(len(self.ranges.ranges), 2)
        
        # Both ranges should be found
        self.assertTrue(self.ranges.find_point(6))   # In first range
        self.assertTrue(self.ranges.find_point(9))   # In both ranges  
        self.assertTrue(self.ranges.find_point(12))  # In second range

class TestRangeEdgeCases(unittest.TestCase):
    """Additional tests for edge cases and error conditions."""
    
    def setUp(self):
        self.ranges = ManageRanges()
    
    def test_boundary_values(self):
        """Test extreme boundary values."""
        # Test with constraint limits
        self.ranges.add(-1000000000, 1000000000)
        
        self.assertTrue(self.ranges.find_point(-1000000000))
        self.assertTrue(self.ranges.find_point(0))
        self.assertTrue(self.ranges.find_point(1000000000))
    
    def test_many_ranges_performance(self):
        """Test performance with many ranges."""
        # Add 100 non-overlapping ranges
        for i in range(0, 1000, 10):
            self.ranges.add(i, i + 5)
        
        self.assertEqual(len(self.ranges.ranges), 100)
        
        # Test some queries
        self.assertTrue(self.ranges.find_point(2))    # In first range
        self.assertTrue(self.ranges.find_point(502))  # In middle range
        self.assertFalse(self.ranges.find_point(506)) # Between ranges

if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)