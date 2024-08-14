class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hash_map[sorted_word].append(word)

        return list(hash_map.values())