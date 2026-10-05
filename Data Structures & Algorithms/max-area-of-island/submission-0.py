class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1,0)]
        #dfs keep track of O(4^n)
        def dfs(r:int, c:int) -> int:
            # base case 1: out of bounds or tile != 1
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
                or grid[r][c] != 1):
                return 0
            # visit tile
            grid[r][c] = -1
            # recursive step: search in every direction
            print("reached")
            ans = 1
            for rdir, cdir in dirs:
                ans += dfs(r+ rdir, c + cdir)
            return ans
        #visit efery node
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
            # call dfs on node with 1
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
            # keep track of max
        return ans
        