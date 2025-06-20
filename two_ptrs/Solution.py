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

