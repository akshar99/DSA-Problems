class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')': '(', '}': '{', ']': '['} 

        for ele in s:

            if ele in mapping.values():
                stack.append(ele)

            else:

                if not stack or stack[-1] != mapping.get(ele, ''):
                    return False
                
                stack.pop()
        return len(stack) == 0