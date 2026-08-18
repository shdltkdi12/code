class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        stack = []
        for letter in s:
            if letter.isdigit() and not stack or (stack and not stack[0].isdigit()):
                substr = []
                while stack:
                    substr.append(stack.pop())
                ans = ''.join(substr) + ans
            elif letter == ']':
                substr = []
                while stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop() # pop [
                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                multiplier = int(''.join(multiplier[::-1]))
                stack.append(''.join(multiplier*substr))
                continue
            stack.append(letter)
        
        ans = ''.join(stack) + ans
        return ans[::-1]
                
