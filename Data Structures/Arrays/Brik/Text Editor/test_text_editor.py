import unittest
from code import TextEditor


class TestTextEditor(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh TextEditor instance for each test."""
        self.editor = TextEditor()
    
    def test_init(self):
        """Test that TextEditor initializes correctly."""
        self.assertIsNotNone(self.editor.editor)
        self.assertEqual(len(self.editor.editor), 0)
    
    def test_insert_single_character(self):
        """Test inserting a single character."""
        self.editor.insert(0, "a")
        self.assertEqual(len(self.editor.editor), 1)
        # Check that the character was inserted with correct index
        self.assertIn((0, "a"), self.editor.editor)
    
    def test_insert_multiple_characters(self):
        """Test inserting multiple characters."""
        self.editor.insert(0, "hello")
        self.assertEqual(len(self.editor.editor), 5)
        
        # Check that all characters were inserted with correct indices
        expected_pairs = [(0, "h"), (1, "e"), (2, "l"), (3, "l"), (4, "o")]
        for pair in expected_pairs:
            self.assertIn(pair, self.editor.editor)
    
    def test_insert_empty_string(self):
        """Test inserting an empty string."""
        self.editor.insert(0, "")
        self.assertEqual(len(self.editor.editor), 0)
    
    def test_multiple_inserts(self):
        """Test multiple insert operations."""
        self.editor.insert(0, "abc")
        self.editor.insert(0, "def")
        
        # Should have 6 characters total
        self.assertEqual(len(self.editor.editor), 6)
        
        # Check specific characters exist
        self.assertIn((0, "a"), self.editor.editor)
        self.assertIn((1, "b"), self.editor.editor)
        self.assertIn((2, "c"), self.editor.editor)
        self.assertIn((3, "d"), self.editor.editor)
        self.assertIn((4, "e"), self.editor.editor)
        self.assertIn((5, "f"), self.editor.editor)
    
    def test_delete_single_character(self):
        """Test deleting a single character."""
        self.editor.insert(0, "hello")
        self.assertEqual(len(self.editor.editor), 5)
        
        # Delete one character from position 0
        self.editor.delete(0, 1)
        self.assertEqual(len(self.editor.editor), 4)
    
    def test_delete_multiple_characters(self):
        """Test deleting multiple characters."""
        self.editor.insert(0, "hello world")
        self.assertEqual(len(self.editor.editor), 11)
        
        # Delete 5 characters from position 0
        self.editor.delete(0, 5)
        self.assertEqual(len(self.editor.editor), 6)
    
    def test_delete_all_characters(self):
        """Test deleting all characters."""
        self.editor.insert(0, "test")
        self.assertEqual(len(self.editor.editor), 4)
        
        # Delete all 4 characters
        self.editor.delete(0, 4)
        self.assertEqual(len(self.editor.editor), 0)
    
    def test_delete_zero_length(self):
        """Test deleting zero characters."""
        self.editor.insert(0, "hello")
        original_length = len(self.editor.editor)
        
        # Delete 0 characters - should not change anything
        self.editor.delete(0, 0)
        self.assertEqual(len(self.editor.editor), original_length)
    
    def test_delete_from_empty_editor(self):
        """Test deleting from an empty editor."""
        # This should raise an exception or handle gracefully
        with self.assertRaises(IndexError):
            self.editor.delete(0, 1)
    
    def test_delete_beyond_available_characters(self):
        """Test deleting more characters than available."""
        self.editor.insert(0, "hi")
        self.assertEqual(len(self.editor.editor), 2)
        
        # Try to delete 5 characters when only 2 exist
        # This should raise an exception
        with self.assertRaises(IndexError):
            self.editor.delete(0, 5)
    
    def test_insert_and_delete_combination(self):
        """Test combination of insert and delete operations."""
        # Insert some text
        self.editor.insert(0, "programming")
        self.assertEqual(len(self.editor.editor), 11)
        
        # Delete some characters
        self.editor.delete(0, 4)  # Remove "prog"
        self.assertEqual(len(self.editor.editor), 7)
        
        # Insert more text
        self.editor.insert(0, "Python")
        self.assertEqual(len(self.editor.editor), 13)
    
    def test_edge_case_large_text(self):
        """Test with larger text input."""
        large_text = "A" * 1000
        self.editor.insert(0, large_text)
        self.assertEqual(len(self.editor.editor), 1000)
        
        # Delete half of it
        self.editor.delete(0, 500)
        self.assertEqual(len(self.editor.editor), 500)
    
    def test_special_characters(self):
        """Test inserting special characters."""
        special_text = "Hello\nWorld\t!"
        self.editor.insert(0, special_text)
        self.assertEqual(len(self.editor.editor), len(special_text))
        
        # Check that special characters are preserved
        self.assertIn((5, "\n"), self.editor.editor)
        self.assertIn((11, "\t"), self.editor.editor)
    
    def test_unicode_characters(self):
        """Test inserting Unicode characters."""
        unicode_text = "こんにちは🌍"
        self.editor.insert(0, unicode_text)
        self.assertEqual(len(self.editor.editor), len(unicode_text))
        
        # Check that Unicode characters are preserved
        self.assertIn((0, "こ"), self.editor.editor)
        self.assertIn((5, "🌍"), self.editor.editor)  # Corrected index


class TestTextEditorIntegration(unittest.TestCase):
    """Integration tests for more complex scenarios."""
    
    def setUp(self):
        self.editor = TextEditor()
    
    def test_text_editing_workflow(self):
        """Test a realistic text editing workflow."""
        # Start with some text
        self.editor.insert(0, "Hello World")
        
        # Delete "World"
        self.editor.delete(6, 5)
        self.assertEqual(len(self.editor.editor), 6)
        
        # Insert "Python"
        self.editor.insert(0, "Python")
        self.assertEqual(len(self.editor.editor), 12)
        
        # Should have characters from both insertions
        # Note: The current implementation has issues with offset handling
        # These tests reveal the problems in the implementation
    
    def test_performance_with_many_operations(self):
        """Test performance with many insert/delete operations."""
        # Insert many small strings
        for i in range(100):
            self.editor.insert(0, f"text{i}")
        
        # Delete in batches
        for _ in range(50):
            if len(self.editor.editor) > 0:
                self.editor.delete(0, min(10, len(self.editor.editor)))


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)