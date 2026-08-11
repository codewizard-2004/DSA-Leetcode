class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make an adjacency list
        adj = [[] for _ in range(n)]

        # set the adj list with values
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        comps = 0
        
        # create the dfs method
        def dfs(node):
            if node in visited or adj[node] == []:
                return
            
            # add node to seen nodes
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        for node in range(n):
            if node not in visited:
                comps += 1
                dfs(node)
        
        return comps
        