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

