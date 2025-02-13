"""
Each number is the sum of two numbers above it return the rows
in a list. 

Every corner element has to be 1 
first two elements can be fixed as [1] and [1,1]

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]*(i+1) for i in range(numRows)]
        
        for i in range(2, numRows):
            for j in range(1,i):
                out[i][j] = out[i-1][j] + out[i-1][j-1]




        return out
