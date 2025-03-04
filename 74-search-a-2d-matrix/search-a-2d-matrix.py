class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1:
            return False
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                if target in row:
                    return True
        return False