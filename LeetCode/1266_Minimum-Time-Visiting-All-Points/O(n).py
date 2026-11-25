""" 1266. Minimum Time Visiting All Points
Author: Mrunal Nirajkumar Shah
Date  : November 24, 2026

Time Complexity : O(n) 
Space Complexity: O(1)

Method: Move (Diagonal - 4 quadrant), (up, down), (left, right) based on two points.
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        count = 0
        for i in range(1, len(points)):
            j = i - 1

            xi = points[i][0]
            yi = points[i][1]
            
            xj = points[j][0]
            yj = points[j][1]

            if xi != xj and yi != yj:
                min_val = min(abs(xi - xj), abs(yi - yj))
                # Up-right
                if xi > xj and yi > yj:
                    xj += min_val
                    yj += min_val
                # Down-left
                elif xi < xj and yi < yj:
                    xj -= min_val
                    yj -= min_val
                # Down-right
                elif xi > xj and yi < yj:
                    xj += min_val
                    yj -= min_val
                # Up-left
                elif xi < xj and yi > yj:
                    xj -= min_val
                    yj += min_val

                count += min_val

            if xi != xj and yi == yj:
                min_val = abs(xi - xj)
                if xi > xj:
                    xj += min_val
                else:
                    xj -= min_val

                count += min_val

            if yi != yj and xi == xj:
                min_val = abs(yi - yj)
                if yi > yj:
                    yj += min_val
                else:
                    yj -= min_val

                count += min_val

        return count

def main():
    list_points = [
        [[1,1],[3,4],[-1,0]],
        [[3,2],[-2,2]],
        [[0, 0], [2, -2]],
        [[0, 0], [1, 1], [4, -2]],
        [[0, 0], [3, -1]]
    ]

    list_output = [
        7,
        5,
        2,
        4,
        3
    ]

    solve = Solution()

    results = []
    for points in list_points:
        results.append(solve.minTimeToVisitAllPoints(points))

    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()