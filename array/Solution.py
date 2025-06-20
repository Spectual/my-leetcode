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


    # 26 Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        cnt = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left = right
                cnt += 1
                nums[cnt-1] = nums[right]
            right += 1
        return cnt


    # 80 Remove Duplicates from Sorted Array II
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2
        i = 2
        while i < len(nums):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k


    # 169 Majority Element
    def majorityElement(self, nums: List[int]) -> int:
        record = defaultdict(int)
        res = 0

        for n in nums:
            record[n] += 1
            if record[n] > len(nums) // 2:
                res = n
        return res


    # 189 Rotate Array
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        res = [0] * n
        for i in range(n):
            res[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = res[i]


    # 121 Best Time to Buy and Sell
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p-buy)
        return profit


    # 274 H-index
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        size = len(citations)

        for i in range(size):
            if citations[i] >= size-i:
                return size - i
        return 0


    # 380 Insert Delete GetRandom O(1)
    class RandomizedSet:

        def __init__(self):
            self.arr = []
            self.pos = {}

        def insert(self, val: int) -> bool:
            if val in self.arr:
                return False
            self.arr.append(val)
            self.pos[val] = len(self.arr)-1
            return True

        def remove(self, val: int) -> bool:
            if val not in self.arr:
                return False
            pos = self.pos[val]
            self.arr[pos] = self.arr[-1]
            self.pos[self.arr[-1]] = pos
            self.arr.pop()
            return True

        def getRandom(self) -> int:
            return random.choice(self.arr)


    # 238 Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = left[:]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        return [x * y for x, y in zip(left, right)]


    # 13 Roman to Integer
    def romanToInt(self, s: str) -> int:
        record = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and record[s[i]] < record[s[i+1]]:
                result += record[s[i+1]] - record[s[i]]
                i += 2
            else:
                result += record[s[i]]
                i += 1
        return result


    # 58 Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        res = 0
        while i >= 0:
            if s[i] != ' ':
                res += 1
            elif res != 0:
                return res
            i -= 1
        return res


    # 14 Longest Common Prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        result = []
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, size):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return "".join(result)
            result.append(c)
        return "".join(result)


    # 28 Find the index of the First Occurence in a String
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        for i in range(len(haystack)-len(needle)+1):
            isPart = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    isPart = False
                    break
            if isPart:
                return i
        return -1