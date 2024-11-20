class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if c == ')':
                    if len(stack) > 0 and stack.pop() == '(':
                        stack.pop()
                    else:
                        return False
                if c == '}':
                    if len(stack) > 0 and stack.pop() == '{':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if len(stack) > 0 and stack.pop() == '[':
                        stack.pop()
                    else:
                        return False

        if(len(stack) == 0):
            return True
        else:
            return False

solution = Solution()
print(solution.isValid('][]'))

# better solution

class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    

solution2 = Solution2()
print(solution2.isValid('()()()(){}{}{}{}{}'))