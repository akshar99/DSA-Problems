class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        max_vol = 0

        while l <r:
            h = min(height[l], height[r])
            w = r - l
            vol = h * w

            max_vol = max(vol, max_vol)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return max_vol