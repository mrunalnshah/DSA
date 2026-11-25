""" 54. Spiral Matrix
Author: Mrunal Nirajkumar Shah
Date  : November 25, 2026

Time Complexity : O(R * C)
Space Complexity: O(1)
where R = number of Rows, and C = number of Columns

Method: Traverse through defined movement - right -> down -> left -> up.
        Keep track of 4 variables to bound the movement 
        (top = 0, bottom = len(matrix), left = 0, right = len(matrix[0]))

        Keep reducing and increasing the bound to shrink it as we traverse.
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        traversed = []

        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        total = len(matrix) * len(matrix[0])

        topBorder = 0
        leftBorder = 0
        rightBorder = n
        bottomBorder = m

        movement = ["right", "down", "left", "up"]

        while len(traversed) != total:
            for traverse_policy in movement:
                if traverse_policy == "right":
                   i = topBorder
                   j = leftBorder

                   while j <= rightBorder:
                      traversed.append(matrix[i][j])

                      j += 1


                   topBorder += 1

                elif traverse_policy == "down":
                    i = rightBorder
                    j = topBorder

                    while j <= bottomBorder:
                        traversed.append(matrix[j][i])

                        j += 1

                    rightBorder -= 1

                elif traverse_policy == "left":
                    i = bottomBorder
                    j = rightBorder

                    while j >= leftBorder:
                        traversed.append(matrix[i][j])

                        j -= 1

                    bottomBorder -= 1

                elif traverse_policy == "up":
                    i = leftBorder
                    j = bottomBorder

                    while j >= topBorder:
                        traversed.append(matrix[j][i])

                        j -= 1

                    leftBorder += 1

                if len(traversed) == total:
                    return traversed
                


def main():
    list_matrix = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ]

    list_output = [
        [1,2,3,6,9,8,7,4,5],
        [1,2,3,4,8,12,11,10,9,5,6,7]
    ]

    solve = Solution()

    results = []
    for matrix in list_matrix:
        results.append(solve.spiralOrder(matrix))

    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()