class Solution:
    # 860 Lemonade Change
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1
            if b == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


    # 406 Queue Reconstruction by Height
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for p in sorted_people:
            result.insert(p[1], p)
        return result


    # 452 Minimum Number of Arrows to Burst Balloons
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        cnt = 1
        min_edge = sorted_points[0][1]
        for p in sorted_points:
            if p[0] <= min_edge and p[1] >= min_edge:
                pass
            elif p[1] < min_edge:
                min_edge = p[1]
            else:
                min_edge = p[1]
                cnt += 1
        return cnt


    # 435 Non-overlapping Intervals
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        min_edge = sorted_intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            if sorted_intervals[i][0] < min_edge:
                cnt += 1
                min_edge = min(min_edge, sorted_intervals[i][1])    
            else:
                min_edge = sorted_intervals[i][1]
        return cnt


    # 763 Partition Labels
    def partitionLabels(self, s: str) -> List[int]:
        record = {}
        result = []
        left = 0
        right = 0
        for i, c in enumerate(s):
            record[c] = i

        for i, c in enumerate(s):
            right = max(right, record[c])
            if i == right:
                result.append(i - left + 1)
                left = i + 1
        return result


    # 56 Merge Intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        result = []

        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                result.append([left, right])
                left = intervals[i][0]
            right = max(right, intervals[i][1])
        result.append([left, right])

        return result


    # 738 Monotone Increasing Digits
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        flag = len(digits)
        if n < 10:
            return n
        for i in range(len(digits)-2, -1, -1):
            if digits[i] > digits[i+1]:
                digits[i] = str(int(digits[i]) - 1)
                flag = i+1
        for i in range(flag, len(digits)):
            digits[i] = str(9)
        return int("".join(digits))