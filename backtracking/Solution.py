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


    # 17 Letter Combinations of a Phone Number
    def backtracking(self, letters, start_index, k, results, path):
        if start_index == k:
            results.append(path)
            return

        for i in range(len(letters[start_index])):
            path += letters[start_index][i]
            self.backtracking(letters, start_index+1, k, results, path)
            path = path[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letter_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digits = [int(c) for c in digits]
        letters = [letter_map[idx] for idx in digits]
        results = []
        path = ""
        self.backtracking(letters, 0, len(digits), results, path)
        return results


    # 39 Combination Sum
    def backtracking(self, candidates, start_index, target, path, result):
        if sum(path) >= target:
            if sum(path) == target:
                result.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, i, target, path, result)
            path.pop()

        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        self.backtracking(candidates, 0, target, path, result)
        return result
    

    # 46 Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtracking(nums, path, res):
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                copy = nums[:]
                copy.pop(i)
                backtracking(copy, path, res)
                path.pop()
        backtracking(nums, path, res)
        return res