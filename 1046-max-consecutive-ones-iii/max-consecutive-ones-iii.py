class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        counter = 0
        max_count = 0

        while right < len(nums):

            if nums[right] == 0:
                counter += 1

            if counter > k:
                if nums[left] == 0:
                    counter -= 1

                left += 1

            if counter <= k:
                max_count = max(right - left + 1,max_count)

            right += 1

        return max_count
