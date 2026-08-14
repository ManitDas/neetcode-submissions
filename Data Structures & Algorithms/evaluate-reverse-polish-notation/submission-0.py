class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                result = a + b
                stack.append(result)
            
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                result = a * b
                stack.append(result)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                result = a - b
                stack.append(result)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                result = int(a / b)
                stack.append(result)

            else:
                stack.append(int(token))

        return stack[-1]      