class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []

        for char in s:
            match char:
                case "(" | "{" | "[":
                    parentheses_stack.append(char)
                case ")":
                    if not parentheses_stack or parentheses_stack.pop() != "(":
                        return False
                case "}":
                    if not parentheses_stack or parentheses_stack.pop() != "{":
                        return False
                case "]":
                    if not parentheses_stack or parentheses_stack.pop() != "[":
                        return False
                case _:
                    continue
        
        return not parentheses_stack
                    