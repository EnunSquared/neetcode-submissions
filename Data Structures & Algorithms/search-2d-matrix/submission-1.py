class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        index = -1
        while top <= bot:
            mid = top + (bot - top) // 2
            print("mid val", mid)
            if mid == len(matrix) - 1 or (matrix[mid][0] < target and matrix[mid + 1][0] > target):
                index = mid
                break
            elif matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1
        print("index is", index)
        if index < 0:
            return False
        
        left = 0
        right = len(matrix[index]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid + 1
            elif matrix[index][mid] > target:
                right = mid - 1

        return False
