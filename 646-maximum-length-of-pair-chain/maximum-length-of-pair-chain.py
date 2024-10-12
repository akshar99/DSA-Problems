class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        chains = 1

        prev_end = pairs[0][1]
        
        for i in range(1, len(pairs)):
            if prev_end < pairs[i][0]:
                chains += 1
                prev_end = pairs[i][1]

            else:
                prev_end = min(prev_end, pairs[i][1])
        return chains