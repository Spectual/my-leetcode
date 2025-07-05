class Solution:

    # All Paths from 1 to N DFS
    result = []
    path = [1]

    # Adjacent matrix   
    def dfs(graph, x, n):
        if x == n:
            result.append(path[:])
            return

        for i in range(1, n+1):
            if graph[x][i] == 1:
                path.append(i)
                dfs(graph, i, n)
                path.pop()

    # Adjacency list
    def dfs(graph, x, n):
        if x == n:
            result.append(path[:])
            return

        for i in graph[x]:
            path.append(i)
            dfs(graph, i, n)
            path.pop()

    # Adjacency matrix
    def main():
        n, m = map(int, input().split())
        graph = [[0] * (n+1) for _ in range(n+1)]

        for i in range(m):
            n1, n2 = map(int, input().split())
            graph[n1][n2] = 1
        
        dfs(graph, 1, n)
        
        if not result:
            print(-1)
        else:
            for i in range(len(result)):
                print(" ".join(map(str, result[i])))

    # Adjacency list
    def main():
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]

        for i in range(m):
            n1, n2 = map(int, input().split())
            graph[n1].append(n2)
        
        dfs(graph, 1, n)
        
        if not result:
            print(-1)
        else:
            for i in range(len(result)):
                print(" ".join(map(str, result[i])))


    #  200 Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        res = 0
        row = len(grid)
        col = len(grid[0])
        if not grid:
            return res

        def dfs(grid, x, y, row, col):
            if x < 0 or x > row - 1 or y < 0 or y > col - 1:
                return
            if grid[x][y] == "0":
                return
            else:
                grid[x][y] = "0"
            dfs(grid, x-1, y, row, col)
            dfs(grid, x, y-1, row, col)
            dfs(grid, x+1, y, row, col)
            dfs(grid, x, y+1, row, col)
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid, i, j, row, col)
        return res   
