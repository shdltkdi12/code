class TextEditor:

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def addText(self, text: str) -> None:
        for char in text:
            self.left_stack.append(char)

    def deleteText(self, k: int) -> int:
        ans = min(k, len(self.left_stack))
        for i in range(min(k, len(self.left_stack))):
            self.left_stack.pop()
        return ans

    def cursorLeft(self, k: int) -> str:
        for i in range(min(k, len(self.right_stack))):
            self.left_stack.append(self.right_stack.pop())

        output = []        
        for i in range(max(0, len(self.left_stack)-11), len(self.left_stack)):
            output.append(self.left_stack[i])
        return ''.join(output)

    def cursorRight(self, k: int) -> str:
        for i in range(min(k, len(self.right_stack))):
            self.right_stack.append(self.left_stack.pop())

        output = []        
        for i in range(max(0, len(self.left_stack)-11), len(self.left_stack)):
            output.append(self.left_stack[i])
        return ''.join(output)

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
