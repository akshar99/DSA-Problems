class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #need to calculate sum of three int , where i!=j, j!=k, k!=i
        """upon transversing the array we also need to skip duplicates
        first thing to do is to sort the array and start the loop with i in range(len(nums))
        left is +1 i and right is last 
        """ 

        nums.sort()
        out = []

        for i in range(len(nums)):

            if i > 0  and nums[i] == nums[i - 1]:
                continue

            l = i +1
            r = len(nums) - 1

            while l < r:
                sums = nums[i] + nums[l] + nums[r]

                if sums == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif sums < 0:
                    l += 1

                else:
                    r -= 1

        return out 
