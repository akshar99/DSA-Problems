class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for ele in arr:
            if ele in hash_map:
                hash_map[ele]  += 1
            else:
                hash_map[ele] = 1
        print(hash_map)
        ls = []
        for value in hash_map.values():
            ls.append(value)

        return len(ls) == len(set(ls))
