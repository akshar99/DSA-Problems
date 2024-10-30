class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        out = []
        closest_sum = float('inf')
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                
                if abs(sum3 - target) < abs(closest_sum - target):
                    closest_sum = sum3

                if sum3 == target:
                    return sum3

                
                elif sum3 < target:
                    l += 1
                else: 
                    r -=1
            
        return closest_sum
