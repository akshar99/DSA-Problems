class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , max_length, zero = 0,0,0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero += 1
            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            max_length = max(max_length, r - l)


        return max_length