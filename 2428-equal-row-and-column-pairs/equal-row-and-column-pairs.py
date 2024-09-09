class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breadth = len(grid[0])

        transformed = [list(row) for row in zip(*grid)]

        counter = 0

        for row in grid:
            for col in transformed:
                if row == col:
                    counter += 1
        return counter
