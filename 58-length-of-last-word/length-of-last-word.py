class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      #  return len(x[-1]) for x in s.split()

      ls = s.split()

      return len(ls[-1])
      