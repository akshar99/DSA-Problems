class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #EDGE CASE :- if rows are one or the numRows is greater than len(s) 
        if numRows == 1 or numRows > len(s):
            return s

        rows = ['']* numRows
        current_row = 0
        switch = False

        for char in s:
            #print(rows)
            rows[current_row] += char

            if current_row ==0 or current_row == numRows - 1:
                switch = not switch

            current_row += 1 if switch else -1

        return ''.join(rows)