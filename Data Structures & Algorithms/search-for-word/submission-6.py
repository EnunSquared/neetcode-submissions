class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find if a word is within a grid
        # keep track of path
        mem = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # dfs algoth O(4^k) 
        # keep track of previous squares with map
        def dfs(row: int, col: int,i: int) -> List[str]:
            # base case 2: out of bounds or square already searched
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or (row, col) in mem:
                print("at row", row,"col", col, "out of bounds or in mem")
                return False
            # base case 1: len == 3 and word not found
            if i == len(word) - 1 and board[row][col] == word[i]:
                print("cur:", board[row][col], "at row", row,"col", col, "true")
                return True 
            # base case 3: len == 3 and word found 
            if board[row][col] != word[i]:
                print("cur:", board[row][col], "at row", row,"col", col, "false")
                return False
            mem.add((row, col))
            print("cur:", board[row][col], "at row", row,"col", col)
            # recursive steps: call in each directions
            ans = False
            for dir in dirs:
                print("going dir", dir, "at row", row, "col",col)
                ans = ans or dfs(row + dir[0], col + dir[1], i + 1)
            mem.remove((row, col))    
            return ans
        
        # call on each square O(n) where n is num or squares total
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    mem = set()
                    found = dfs(i, j, 0)
                    if found:
                        return True
        return False