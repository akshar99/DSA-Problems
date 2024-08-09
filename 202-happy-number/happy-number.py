class Solution:
    def isHappy(self, n: int) -> bool:
        def generate_num(n):
            return [int(digit) for digit in str(n)]
        
        seen = set()

        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(x**2 for x in generate_num(n))

        return n == 1