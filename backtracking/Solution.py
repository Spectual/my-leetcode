class Solution:
    # 77 Combinations
    def __init__(self):
        self.result = []
        self.path = []
    
    def backtracking(self, n: int, start_index: int, k: int):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        
        for i in range(start_index, n-(k-len(self.path))+2):
            self.path.append(i)
            self.backtracking(n, i+1, k)
            self.path.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(n, 1, k)
        return self.result