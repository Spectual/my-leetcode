class Solution:
    # 242 Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:   
        record = [0] * 26
        for c in s:
            record[ord(c)-ord('a')] += 1
        for c in t:
            record[ord(c)-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True


    # 349 Intersection of Two Arrays
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = defaultdict(int)
        result = set()
        for i in nums1:
            record[i] += 1
        for i in nums2:
            if record[i] > 0:
                result.add(i)
        return list(result)


    # 202 Happy Number
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            new_n = 0
            if n == 1:
                return True
            while n > 0:
                n, r = divmod(n, 10)
                new_n += r ** 2
            
            n = new_n
            if n in record:
                return False
            else:
                record.add(n)


    # 1 Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for i, n in enumerate(nums):
            if target - n in record:
                return [record[target-n], i]
            record[n] = i
        return []