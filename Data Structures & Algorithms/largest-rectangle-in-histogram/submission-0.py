class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            start = index

            while stack and height < stack[-1][1]:
                pop_index, pop_height = stack.pop()
                area = pop_height * (index - pop_index)
                max_area = max(area, max_area)

                start = pop_index
            stack.append([start, height])
        
        for start,height in stack:
            area = height * (len(heights) - start)
            max_area = max(area, max_area)
        
        return max_area