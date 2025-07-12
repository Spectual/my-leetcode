class Solution:
    # 3 Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        record = set()
        left = 0

        for i in range(len(s)):
            while s[i] in record:
                record.remove(s[left])
                left += 1
            record.add(s[i])
            size = max(i-left+1, size)
        return size
