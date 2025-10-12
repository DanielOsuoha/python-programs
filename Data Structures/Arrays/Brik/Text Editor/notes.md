## Problem: Design a Simple Text Editor

### Description
You are tasked with implementing a **simple text editor** that can efficiently handle large amounts of text. The editor should support two main operations:

1. **Insert(offset, text)** – Insert the given `text` starting at the specified `offset` within the current document.
2. **Delete(offset, length)** – Delete `length` characters from the document, starting at the specified `offset`.

The goal is to design and implement a class that supports these operations efficiently, considering that the document can grow to **millions of characters**.

---

### Example

```python
editor = TextEditor()
editor.insert(0, "Hello World")
editor.delete(5, 1)
editor.insert(5, ",")
print(editor.get_text())   # Output: "Hello,World"
