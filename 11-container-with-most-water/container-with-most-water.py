class Solution:
    def maxArea(self, height: List[int]) -> int:
        #in this case we initate two pointers , left at 0 and right at the end 
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l

            max_area = max(max_area, h * w)

            if height[r] < height[l]:
                r -=1

            else:
                l += 1

        return max_area