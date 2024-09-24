class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]

            if S > k:
                r -= 1
            elif S < k:
                l += 1

            else:
                counter += 1
                l += 1
                r -= 1

        return counter