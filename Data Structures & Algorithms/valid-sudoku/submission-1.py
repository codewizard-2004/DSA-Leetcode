class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for all the rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # Check if all columns are valid
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # Check for each square
        squares = {}
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                R = r // 3
                C = c // 3
                if (R, C) not in squares:
                    squares[(R,C)] = set()
                if val in squares[(R,C)]:
                    return False
                squares[(R, C)].add(val)
        
        return True
        