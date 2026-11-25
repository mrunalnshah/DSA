""" 1365. How Many Numbers Are Smaller Than the Current Number
Author: Mrunal Nirajkumar Shah
Date  : November 20, 2026

Time Complexity : O(n^2)
Space Complexity: O(1)

Method: For every num, check which nums are smaller than it. 
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counting_smaller = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[j] < nums[i]:
                    count += 1

            counting_smaller.append(count)

        return counting_smaller

def main():
    list_nums = [
        [8,1,2,2,3],
        [6,5,4,8],
        [7,7,7,7]
    ]

    list_outputs = [
        [4,0,1,1,3],
        [2,1,0,3],
        [0,0,0,0]
    ]

    solve = Solution()

    results = []

    for nums in list_nums:
        results.append(solve.smallerNumbersThanCurrent(nums))

    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()