class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        chars = ['+', '-', '*', '/']
        
        for t in tokens:
            if t not in chars:
                stack.append(t)

            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if t == '+':
                    stack.append(a + b)

                elif t =='-':
                    stack.append(a-b)

                elif t == '*':
                    stack.append(int(a*b))

                elif t=='/':
                    stack.append(int(a/b))

        return int(stack.pop())


