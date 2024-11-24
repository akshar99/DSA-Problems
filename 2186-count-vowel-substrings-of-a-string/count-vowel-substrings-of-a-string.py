class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0 

        for i in range(len(word)):
            seen = set()

            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    seen.add(word[j])

                    if len(seen) >= 5:
                        count += 1
                else:
                    break

        return count

