""" 1. Two Sum
Author: Mrunal Nirajkumar Shah
Date  : November 16, 2026

Time Complexity : O(n^2)
Space Complexity: O(1)

Method: For every ith num, add jth num to if they add to target 
        which is j > i and j < len(nums)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def main():
    list_inputs = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6)
    ]

    list_outputs = [
        [0,1],
        [1,2],
        [0,1]
    ]

    solve = Solution()

    results = []
    for inputs in list_inputs:
        results.append(solve.twoSum(inputs[0], inputs[1]))

    for result, output in zip(results, list_outputs):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")


if __name__ == "__main__":
    main()