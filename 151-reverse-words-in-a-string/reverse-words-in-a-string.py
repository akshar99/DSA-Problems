class Solution:
    def reverseWords(self, s: str) -> str:
        ls =s.split()

        return ' '.join(ls[::-1])