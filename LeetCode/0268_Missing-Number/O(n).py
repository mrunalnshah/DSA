""" 268. Missing Number
Author: Mrunal Nirajkumar Shah
Date  : November 15, 2026

Time Complexity : O(n)
Space Complexity: O(1)

Method: Find Expected_value using n * (n + 1) // 2 and calculate actual sum. 
        the difference of expected and actual, will be the missing value.
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        expected_value = (n * (n + 1)) // 2
        actual_value = 0

        for i in range(n):
            actual_value += nums[i]

        difference = expected_value - actual_value # expected_value >= actual_value

        return difference
    
def main():
    list_nums = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1],
        [0, 1, 2, 3, 4, 5, 6],
        [5, 4, 3, 2, 1]
    ]

    list_output = [
        2,
        2,
        8,
        7,
        0
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.missingNumber(nums))

    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()