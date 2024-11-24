class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_set = {}
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 1
        out = []
        for key,value in hash_set.items():
            if value > 1:
                out.append(key)
        #print(hash_set)
        return out