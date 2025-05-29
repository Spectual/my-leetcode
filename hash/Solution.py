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