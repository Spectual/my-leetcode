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

