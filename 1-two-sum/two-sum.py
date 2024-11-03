class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #x + y = target 
        #target  - x = y
        #create a hash map here 
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return(seen[diff], i)
            
            seen[num] = i