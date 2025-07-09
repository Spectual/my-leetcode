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


    # 11 Contain With Most Water
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while right >= left:
            area = max((right-left)*min(height[left], height[right]), area)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        return area
    

    # 167 Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while right > left:
            if target - numbers[right] == numbers[left]:
                return [left+1, right+1]
            elif target - numbers[right] > numbers[left]:
                left += 1
            else:
                right -= 1

        
    # 15 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):

            if nums[i] > 0:
                return result
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    right -= 1
                    left += 1
                    
        return result
    

    # 42 Trapping Rain Water (Two Pointers)
    def trap(self, height: List[int]) -> int:
        vol = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[left])
                vol += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                vol += rightMax - height[right]
                right -= 1

        return vol