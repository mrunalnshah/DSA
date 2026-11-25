""" 1365. How Many Numbers Are Smaller Than the Current Number
Author: Mrunal Nirajkumar Shah
Date  : November 20, 2026

Time Complexity : O(nlogn)
Space Complexity: O(2 * n) ~ O(n)

Method: Sort nums, and store each distinct value of sorted nums to its index, no duplicates. 
        Return hash_map[num] for each num to get smaller than count for each num.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp_nums = sorted(nums)

        hash_map = {}

        for i, num in enumerate(temp_nums):
            if num not in hash_map:
                hash_map[num] = i

        result = []

        for num in nums:
            result.append(hash_map[num])

        return result

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