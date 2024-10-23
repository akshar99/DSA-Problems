class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        max_vol = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            vol = h * w

            max_vol = max(vol, max_vol)

            if height[right] < height[left]:
                right -=1

            else:
                left += 1

        return max_vol
            