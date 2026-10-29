class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                first_pop = stack.pop()
                second_pop = stack.pop()
                result = 0
                if i == "+":
                    result = first_pop + second_pop
                    stack.append(result)
                elif i == "-":
                    result = second_pop - first_pop
                    stack.append(result)
                elif i == "*":
                    result = second_pop * first_pop
                    stack.append(result)
                else:
                    result = int(second_pop / first_pop)
                    stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]