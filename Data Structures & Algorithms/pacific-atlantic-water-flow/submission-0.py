class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()

        def dfs(r, c, visited, preVal):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                heights[r][c] < preVal or
                (r, c) in visited
            ):
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
            
        
        # Performing dfs from all top and bottom cells
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # Performing dfs from all cells in left and right
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
        