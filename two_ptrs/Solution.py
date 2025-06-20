class Solution:
    # 125 Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        s = s.lower()
        while right >= left:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


    # 392 Is Subsequence
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if s == "":
            return True
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            if i >= len(s):
                return True
            j += 1
            
        return False