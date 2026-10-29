class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in '([{':
                stack.append(i)
            
            if i in '}])':
                if len(stack) != 0 and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0