class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if c == ')':
                    if len(stack) > 0 and stack[len(stack)-1] == '(':
                        stack.pop()
                    else:
                        return False
                if c == '}':
                    if len(stack) > 0 and stack[len(stack)-1] == '{':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if len(stack) > 0 and stack[len(stack)-1] == '[':
                        stack.pop()
                    else:
                        return False

        if(len(stack) == 0):
            return True
        else:
            return False
