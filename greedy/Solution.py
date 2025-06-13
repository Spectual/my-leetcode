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