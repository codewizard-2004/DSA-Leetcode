class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create the adja list
        adj = [ [] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                # found cycle
                return False
            visited.add(node)
            # If node has no nei then return
            if adj[node] == []:
                return True
            
            # do dfs on all neighbours
            for nei in adj[node]:
                if nei != prevNode and not dfs(nei, node):
                    return False
            
            return True

        # if length of visited is not n then there are unconnected components
        if not dfs(0, 0) or len(visited) != n:
            return False
        
        return True
        
        