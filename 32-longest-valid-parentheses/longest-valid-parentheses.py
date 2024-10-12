class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0
        
        stack = []
        stack.append(-1)

        max_len = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
