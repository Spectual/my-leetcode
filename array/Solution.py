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