class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: DFS function to explore the graph
        def dfs(current, destination, visited):
            if current == destination:
                return True
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    if dfs(neighbor, destination, visited):
                        return True
            return False
        
        # Step 3: Use DFS starting from the source
        visited = set()
        return dfs(source, destination, visited)