class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s2 = ''
        out_s = []
        out = []
        for i in range(len(s)):
            if s[i] in vowels:
                s2 = s2 + '~'
                out_s.append(s[i])
            else:
                s2 = s2 + s[i]
        
        for i in range(len(s2)):
            if s2[i] == '~':
                out.append(out_s[-1])
                out_s.pop()
            else:
                out.append(s2[i])

        return ''.join(out)