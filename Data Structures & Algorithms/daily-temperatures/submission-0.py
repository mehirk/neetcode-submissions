class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop_index = stack.pop()
                ans[pop_index] = i - pop_index
            
            stack.append(i)
        
        return ans
