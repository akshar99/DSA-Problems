class Solution:
    def simplifyPath(self, path: str) -> str:
        
        files = []

        path = path.split("/")

        for ele in path:
            if files and ele =='..':
                print(f"popping :: {ele} \n {files}")
                files.pop()
            elif ele not in ['.', '..', '']:
                print(f"appending :: {ele} \n {files}")
                files.append(ele)

        return '/' + '/'.join(files)