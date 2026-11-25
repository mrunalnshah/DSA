""" 1. Two Sum
Author: Mrunal Nirajkumar Shah
Date  : November 16, 2026

Time Complexity : O(n)
Space Complexity: O(n)

Method: Use hashmap to keep track of elements and check if diff exists.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash_map:
                j = hash_map[diff]
                return [i, j]

            hash_map[num] = i

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