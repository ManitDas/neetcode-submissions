class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in pairs:
                if stack and pairs[char] == stack[-1]:
                    stack.pop() 
                else:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0  