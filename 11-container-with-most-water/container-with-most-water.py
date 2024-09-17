class Solution:
    def maxArea(self, height: List[int]) -> int:
        #we will follow two pointer approach here 
        #initiate Left and Right
        L = 0
        R = len(height) - 1
        max_area = 0

        while L < R:
            h = min(height[L], height[R])
            w = R - L
            max_area = max(h*w, max_area)

            if height[R] < height[L]:
                R -= 1

            else:
                L += 1

        return max_area

