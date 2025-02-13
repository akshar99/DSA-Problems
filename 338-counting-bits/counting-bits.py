class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            print(i)
            out.append(bin(i)[2:])
        out2 = []

        for i in range(len(out)):
            num = 0
            num = sum(1 for x in out[i] if int(x) == 1)
            out2.append(num) 
        
        return out2