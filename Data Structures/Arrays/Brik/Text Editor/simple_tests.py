"""
Simple test file to verify TextEditor functionality and identify issues.
Run with: python simple_tests.py
"""

from code import TextEditor

def test_basic_functionality():
    """Test basic insert and delete operations."""
    print("Testing TextEditor basic functionality...")
    
    editor = TextEditor()
    
    print(f"Initial state - Length: {len(editor.editor)}")
    assert len(editor.editor) == 0, "Editor should start empty"
    
    editor.insert(0, "A")
    print(f"After inserting 'A' - Length: {len(editor.editor)}")
    print(f"Contents: {list(editor.editor)}")
    
    editor.insert(0, "BC")
    print(f"After inserting 'BC' - Length: {len(editor.editor)}")
    print(f"Contents: {list(editor.editor)}")
    
    try:
        editor.delete(0, 1)
        print(f"After deleting 1 char from pos 0 - Length: {len(editor.editor)}")
        print(f"Contents: {list(editor.editor)}")
    except Exception as e:
        print(f"Error during delete: {e}")
    
    print("Basic functionality test completed!\n")

def test_implementation_issues():
    """Test to identify issues in the current implementation."""
    print("Testing for implementation issues...")
    
    editor = TextEditor()
    
    print("Issue 1: Insert method ignores offset parameter")
    editor.insert(5, "Hello") 
    print(f"Inserted 'Hello' at offset 5, but indices start at: {[item[0] for item in editor.editor]}")
    
    print("\nIssue 2: Multiple inserts create overlapping indices")
    editor2 = TextEditor()
    editor2.insert(0, "ABC")
    editor2.insert(0, "DEF") 
    print(f"After two inserts, all indices: {[item[0] for item in editor2.editor]}")
    
    print("\nIssue 3: Delete method issues")
    editor3 = TextEditor()
    editor3.insert(0, "ABCDE")
    print(f"Before delete: {list(editor3.editor)}")
    try:
        editor3.delete(1, 2)  
        print(f"After delete(1, 2): {list(editor3.editor)}")
    except Exception as e:
        print(f"Delete failed with error: {e}")
    
    print("Implementation issues test completed!\n")

def test_expected_vs_actual():
    """Compare expected behavior vs actual behavior."""
    print("Testing expected vs actual behavior...")
    
    editor = TextEditor()
    
    print("Expected behavior: Insert 'Hello' at position 0 should create indices 0,1,2,3,4")
    editor.insert(0, "Hello")
    actual_indices = [item[0] for item in editor.editor]
    print(f"Actual indices: {actual_indices}")
    
    print(f"Expected: [0,1,2,3,4], Actual: {actual_indices}")
    print(f"Match: {actual_indices == [0,1,2,3,4]}")
    
    print("Expected vs actual test completed!\n")

def run_all_tests():
    """Run all simple tests."""
    print("=" * 50)
    print("RUNNING SIMPLE TESTS FOR TEXT EDITOR")
    print("=" * 50)
    
    test_basic_functionality()
    test_implementation_issues()
    test_expected_vs_actual()
    
    print("=" * 50)
    print("ALL SIMPLE TESTS COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()