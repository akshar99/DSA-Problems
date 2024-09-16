class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for n in nums:
            print(n)
            if n <= first:
                print("first")
                print(first)
                first = n

            elif n <= second:
                print("second")
                print(second)
                second = n

            else:
                return True

        return False
"""
This is the output

The logic behind is that we should find the third element that is bigger that second
and second is bigger than first, if it encounters any number that is bigger than second it 
return TRUE

First Iteration:
    1
    first
    inf

Second Iteration:
    2
    second
    inf

Third Iteration:
3
"""