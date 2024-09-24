class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set('aeiou')
        left = 0
        right = k
        sub_count = sum(1 for x in s[left:right] if x in vowels)
        max_count = sub_count

        while left < right and right < len(s):

            if s[right] in vowels:
                sub_count += 1
            
            if s[left] in vowels:
                sub_count -= 1

            max_count = max(max_count, sub_count)
            left += 1
            right += 1

        return max_count



