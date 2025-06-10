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


    #216 Combination Sum III
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(n, 1, k)
        return self.result

        def backtracking(self, start_index: int, k: int, n: int, path: List[int], result: List[List[int]]):
        if len(path) == k:
            if sum(path) == n:
                result.append(path[:])
            return
        
        for i in range(start_index, 10):
            path.append(i)
            self.backtracking(i+1, k, n, path, result)
            path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(1, k, n, path, result)
        return result