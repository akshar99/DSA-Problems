class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0

        l = 0
        r = len(nums) - 1

        while  l < r:
            s = nums[l] + nums[r]

            if s < k:
                l += 1
            elif s > k:
                r -= 1

            else:
                counter += 1
                l += 1
                r -=1

        return counter