class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        1- calculate the num from digits and increment 1 
        2- change the output number to list 
        """
        digits[-1] = digits[-1] + 1
        l = len(digits) - 1
        out = 0
        for i in range(len(digits)):
            out  = out + digits[i] * 10 ** l
            l -= 1

        return [int(x) for x in str(out)]