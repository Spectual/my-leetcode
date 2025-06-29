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


    # 62 Unique Paths II
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break    
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break    
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    

    # 343 Integer Break
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[2] = 1
        
        for i in range(3, n+1):
            for j in range(1, i // 2 + 1):
                dp[i] = max([j * (i - j), j * dp[i - j], dp[i]])
        return dp[n]
    

    # 96 Unique Binary Search Trees
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
    
    # 0-1 Knapsack Problem (ACM)
    def knapsack():
        n, bagweight = map(int, input().split())
        weight = list(map(int, input().split()))
        value = list(map(int, input().split()))

        dp = [[0] * (bagweight+1) for _ in range(n)]

        for j in range(weight[0], bagweight+1):
            dp[0][j] = value[0]

        for i in range(1, n):
            for j in range(1, bagweight+1):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], value[i]+dp[i-1][j-weight[i]])
        print(dp[n-1][bagweight])


    # 416 Partition Equal Subset Sum
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = [0] * 10001
        target = sum(nums) // 2

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[target] == target
