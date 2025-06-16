class Solution:
    # 704 Binary Search
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            if target == nums[mid]:
                return mid
        return -1


    # 27 Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


    # 977 Squares of a Sorted Array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        left = 0
        right = len(nums) - 1
        i = right
        while left <= right:
            if nums[right]*nums[right] > nums[left]*nums[left]:
                result[i] = nums[right]*nums[right]
                right -= 1
            else:
                result[i] = nums[left]*nums[left]
                left += 1
            i -= 1
        return result



    # 209 Minimum Size Subarray Sum
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        temp = 0
        result = float('inf')

        for right in range(len(nums)):
            temp += nums[right]
            while temp >= target:
                result = min(result, right - left + 1)
                temp -= nums[left]
                left += 1
        return 0 if result == float('inf') else result


    # 66 Plus One
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        size = len(digits)
        for i in range(size):
            num += digits[size-1-i] * (10 ** i)
        num += 1
        result = []
        while num > 0:
            result.append(num % 10)
            num = num // 10
        
        return result[::-1]


    # 88 Merged Sorted Array
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p >= 0:
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
