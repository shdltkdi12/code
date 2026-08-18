class TextEditor:

    def __init__(self):
        self.editor = []
        self.index =0

    def addText(self, text: str) -> None:
        for i in range(len(text)-1, -1, -1):
            self.editor.insert(self.index, text[i])
        self.index += len(text)

    def deleteText(self, k: int) -> int:
        new_index = max(0, self.index - k)
        self.editor = self.editor[0:new_index] + self.editor[self.index:]
        ans = self.index if new_index == 0 else k
        self.index = new_index
        return ans

    def cursorLeft(self, k: int) -> str:
        self.index = max(0, self.index - k)
        return ''.join(self.editor[max(0, self.index-10):self.index])

    def cursorRight(self, k: int) -> str:
        self.index = min(len(self.editor), self.index + k)
        return ''.join(self.editor[max(0, self.index-10):self.index])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
