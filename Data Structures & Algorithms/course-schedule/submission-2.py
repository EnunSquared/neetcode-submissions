class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            adj[course].append(pre)

        #dfs keep track of whiche course O(v + e)
        def dfs(course: int) -> bool:
            # base case 1: no prerequisites left
            print(adj[course], visited)
            if not adj[course]:
                return True
            # base case 2: course visited
            if course in visited:
                return False
            # visit node
            visited.add(course)
            res = True
            # recursive step: visit all neighbors
            for neigh in adj[course]:
                res = res and dfs(neigh)
            # unvisit node and remove neighbors
            visited.remove(course)
            adj[course] = []
            return res
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True