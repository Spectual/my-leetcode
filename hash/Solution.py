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


    # 454 4Sum
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = defaultdict(int)

        for n1 in nums1:
            for n2 in nums2:
                record[n1+n2] += 1

        result = 0
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in record:
                    result += record[0-n3-n4]
        return result


    # 383 Ransom Note
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = defaultdict(int)

        for c in magazine:
            record[c] += 1
        
        for c in ransomNote:
            record[c] -= 1
            if record[c] < 0:
                return False
        return True
    

    # 205 Isomorphic Strings
    def isIsomorphic(self, s: str, t: str) -> bool:
        record_s = {}
        record_t = {}

        for i in range(len(s)):
            if s[i] not in record_s:
                record_s[s[i]] = i
            if t[i] not in record_t:
                record_t[t[i]] = i
            if record_s[s[i]] != record_t[t[i]]:
                return False
        return True
    

    # 290 Word Pattern
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        record_p = {}
        record_s = {}
        if len(s) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in record_p:
                record_p[pattern[i]] = i
            if s[i] not in record_s:
                record_s[s[i]] = i
            if record_p[pattern[i]] != record_s[s[i]]:
                return False
        return True