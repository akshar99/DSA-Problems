class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        chars = ['+', '-', '*', '/']
        
        for t in tokens:
            #check if not arithmetic operators append the numbers
            if t not in chars:
                stack.append(t)

            else:
                #pop 2 values for operations
                b = int(stack.pop())
                a = int(stack.pop())

                #perform operations as per operations
                if t == '+':
                    stack.append(a + b)

                elif t =='-':
                    stack.append(a-b)

                elif t == '*':
                    stack.append(int(a*b))

                elif t=='/':
                    stack.append(int(a/b))

        return int(stack.pop())


