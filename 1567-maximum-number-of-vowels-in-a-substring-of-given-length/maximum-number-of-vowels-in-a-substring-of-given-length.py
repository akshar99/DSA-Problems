class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set('aeiou')
        l = 0
        r = k
        sub_count = sum(1 for x in s[l:r] if x in vowels)
        max_count = sub_count

        while l < r and r < len(s):

            if s[r] in vowels:
                sub_count += 1
            if s[l] in vowels:
                sub_count -=1

            max_count = max(max_count, sub_count)

            l += 1
            r += 1

        return max_count


