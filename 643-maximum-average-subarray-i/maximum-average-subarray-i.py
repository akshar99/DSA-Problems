class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k]) 
        max_sum = current_sum

        for right in range(k, len(nums)):
            current_sum += nums[right] - nums[right -k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
