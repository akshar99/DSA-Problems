class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)#inititate a false array that we can modify later
        dp[0] = True #first segment will always be true as it is empty

        for i in range(1, len(s)+1): #iterate in i this will help us update the elemnts of dp as true or false
            for word in wordDict:
            #we are checking if the substring just before the currrent string can be segmentes
                if i >= len(word) and s[i - len(word): i] == word:
                    if dp[i - len(word)] == True:
                        dp[i] = True
                        break

        return dp[-1]