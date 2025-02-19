class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = float('-inf')

        right = s.count('1')
        left = 0
        for i in range(len(s) - 1):

            if s[i] == '0':
                left += 1
            else:
                right -= 1

            maxScore = max(maxScore, (left+ right))
        
        return maxScore
