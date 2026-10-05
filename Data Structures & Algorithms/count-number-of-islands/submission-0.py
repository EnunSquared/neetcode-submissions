class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1,0), (-1, 0)]
        # dfs keep track of index O(n)
        # turn connected 1s into hashes
        def dfs(row:int, col:int):
            # base case 1: out of bounds or 0
            if (row < 0 or row >= len(grid) or col < 0 or 
                    col >= len(grid[0]) or grid[row][col] != '1'):
                return
            # replace 1 with hash
            grid[row][col] = '#'
            # recursive step: call dfs in all four directions
            for dir in dirs:
                dfs(row + dir[0], col + dir[1])

        ans = 0
        #explore entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # call dfs if 1 is found
                if grid[i][j] == '1':
                    # increae number if islands found
                    ans += 1
                    dfs(i, j)
        return ans