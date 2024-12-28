class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_map = {}

        s1 ,s2 = set(nums1), set(nums2)

        ans = [[], []]

        for ele in s1:
            if ele not in s2:
                ans[0].append(ele)

        for elem in s2:
            if elem not in s1:
                ans[1].append(elem)

        return ans