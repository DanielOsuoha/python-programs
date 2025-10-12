class TextEditor:
    from sortedcontainers import SortedList
    def __init__(self):
        self.editor = SortedList()
    
    def insert(self, offset, text):
        index = len(self.editor)
        for i in range(len(text)):
            self.editor.add((index+i, text[i]))

    def delete(self, offset, length):
        pass