from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash_set = defaultdict(int)
        #if the length is not even then it is false
        if len(arr) % 2 != 0:
            return  False
        # we default dict as it automatically handles the error and increment and update value 
        #if present or not 
        for num in arr:
            reminder = num % k
            hash_set[reminder] += 1
        #now iterate over the hash set values
        for rem in hash_set:
        #if reminder is zero that means it should have equal no of elements that should have zero reminder
            if rem == 0:
                if hash_set[rem] % 2 != 0:
                    return False
        #if it is of half the size of k that also means it should have same number of elements
            elif rem * 2 == k:
                if hash_set[rem]  %2 != 0:
                    return False
        # no of reminder are to be equal to no of reminders for k - rem also
            else:
                if hash_set[rem] != hash_set[k - rem]:
                    return False

        #otherwise return true
        return True