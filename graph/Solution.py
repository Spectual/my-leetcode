from typing import List, Optional
from collections import deque

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


    # 130 Surrounded Regions 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        que = deque()

        for i in range(m):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][n-1] == "O":
                que.append((i, n-1))
        for j in range(n):
            if board[0][j] == "O":
                que.append((0, j))
            if board[m-1][j] == "O":
                que.append((m-1, j))

        while que:
            r, c = que.popleft()
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                board[r][c] = "#"
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    que.append((r+dr, c+dc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
    

    # 133 Clone Graph
    """
    # Definition for a Node.
    class Node:
        def __init__(self, val = 0, neighbors = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []
    """
    def __init__(self):
        self.record = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        def dfs(node):
            if node in self.record:
                return self.record[node]
            
            copy = Node(node.val)
            self.record[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        copy = dfs(node)
        return copy
    

    # 433 Minimum Genetic Mutation
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)

        if endGene not in bank and startGene != endGene:
            return -1

        que = deque([(startGene, 0)])
        visited = {startGene}
        while que:
            gene, d = que.popleft()
            if gene == endGene:
                return d
            for i in range(8):
                for c in ['A', 'C', 'G', 'T']:
                    mut = gene[:i] + c + gene[i+1:]
                    if mut in bank and mut not in visited:
                        visited.add(mut)
                        que.append((mut, d+1))
        return -1