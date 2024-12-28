class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, counter, max_count = 0, 0, 0, float('-inf')

        while r < len(nums):

            if nums[r] == 0:
                counter += 1
            
            if counter > k:
                if nums[l] ==0:
                    counter -=1
                
                l += 1

            if counter <= k:
                max_count = max(r - l + 1, max_count)
            r += 1

        return max_count
