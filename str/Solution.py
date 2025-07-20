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


    # 5 Longest Palindromic Substring
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, l: int, r: int):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        n = len(s)
        start = 0
        end = 0
        for i in range(n):
            even = expand_around_center(s, i, i+1)
            odd = expand_around_center(s, i, i)
            max_len = max(even, odd)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]