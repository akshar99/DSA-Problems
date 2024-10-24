class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_stack = []
        path = path.split("/")
        
        for ele in path:
            if dir_stack and ele=='..':
                dir_stack.pop()

            elif ele not in ['.', '..', '']:
                dir_stack.append(ele)

        return "/" + "/".join(dir_stack)