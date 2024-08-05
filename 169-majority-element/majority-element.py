class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_map = {item: nums.count(item) for item in set(nums)}
        max_key = max(counter_map, key=counter_map.get)
        return max_key

        