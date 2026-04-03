import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                if token in ["+", "-", "*", "/"]:
                    num2 = stack.pop()
                    num1 = stack.pop()

                    match token:
                        case "+":
                            stack.append(num1 + num2)
                        case "-":
                            stack.append(num1 - num2)
                        case "*":
                            stack.append(num1 * num2)
                        case "/":
                            stack.append(int(num1 / num2))
                        case _:
                            pass
        
        return stack[-1]
        