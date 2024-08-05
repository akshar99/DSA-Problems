class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = int(len(nums))
        k = k % l
        split_val = l - k
        new_sublist = nums[0:split_val]
        nums[0:split_val] = []
        nums.extend(new_sublist)
        