class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        out = [0] *(n+1)

        for i in range(1, n + 1):
            out[i] = out[i-1] + gain[i - 1]
        return max(out)