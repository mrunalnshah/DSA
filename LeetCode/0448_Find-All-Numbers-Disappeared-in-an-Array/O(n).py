""" 448. Find All Numbers Disappeared in an Array
Author: Mrunal Nirajkumar Shah
Date  : November 15, 2026

Time Complexity : O(2 * n) ~ O(n)
Space Complexity: O(n)

Method: Insert all unique values in hash_map while keeping track of how many duplicates.
        Loop through 1 to n, and check if i in hash_map, if not add it to missing list, 
        else continue.
"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        hash_map = {}

        duplicates = 0
        for num in nums:
            if num in hash_map:
                duplicates += 1
            else:
                hash_map[num] = 1

        missing = []
        for i in range(1, len(nums) + 1):
            if i in hash_map:
                continue
            else:
                missing.append(i)

        return missing

def main():
    list_nums = [
        [4,3,2,7,8,2,3,1],
        [1,1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    list_outputs = [
        [5,6],
        [2],
        [2, 3, 4, 5, 6, 7]
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.findDisappearedNumbers(nums))

    for result, output in zip(results, list_outputs):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()