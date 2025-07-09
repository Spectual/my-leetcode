class Solution:
    # 739 Daily Temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res