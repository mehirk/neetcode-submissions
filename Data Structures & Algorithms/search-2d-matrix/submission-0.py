class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix) #Total number of rows
        n = len(matrix[0]) #Total number of columns

        left = 0
        right = m*n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False