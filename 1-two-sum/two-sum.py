class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}


        for i, ele in enumerate(nums):
            complement  = target - ele
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[ele] = i


"""
BRUTE FORCE Failed approacj
        for ele in nums:
            hash_map(ele) = target - ele

        for key, val in enumerate(hash_map):
            if val in nums:
                return [key, val]

"""