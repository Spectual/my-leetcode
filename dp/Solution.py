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


    # 1049 Last Stone Weight II
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [0] * 1501
        total = sum(stones)
        target = total // 2
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return total - dp[target] - dp[target]
    

    # 91 Decode Ways
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            one = int(s[i-1])
            two = int(s[i-2:i])
            if one in range(1, 10):
                dp[i] += dp[i-1]
            if two in range(10, 27):
                dp[i] += dp[i-2]
        return dp[n]


    # 120 Triangle
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = 0
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
        for i in range(1, n):
            dp[i][i] = triangle[i][i] + dp[i-1][i-1]
        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[n-1])
    

    # 72 Edit Distance
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:    
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
        return dp[m][n]
    

    # 97 Interleaving String
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
            
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])

        return dp[m][n]
    

    # 221 Maximal Square
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_len = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                        ) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len ** 2
