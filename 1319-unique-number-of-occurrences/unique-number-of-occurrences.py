class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_set = {}
        for num in arr:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 0

        seen = []

        for key, value in hash_set.items():
            if value in seen:
                return False
            else:
                seen.append(value)

        return True
