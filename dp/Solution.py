class Solution:
    # 509 Fibonacci Number
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1 

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


    # 70 Climbing Stairs
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


    # 746 Min Cost Climbing Stairs
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]


    # 62 Unique Paths
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]