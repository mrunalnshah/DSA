""" 268. Missing Number
Author: Mrunal Nirajkumar Shah
Date  : November 15, 2026

Time Complexity : O(n^2)
Space Complexity: O(1)

Method: Looping through i to len(nums) for each i is a unique value; nested loop checks i in array. 
        if found, we continue, we not we return i. if not found till the end, we know its len(nums)
        missing.
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            is_found = False
            for j in range(len(nums)):
                if i == nums[j]:
                    is_found = True
                    continue

            if is_found == False:
                return i

        return len(nums)

def main():
    list_nums = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1]
    ]

    list_output = [
        2,
        2,
        8
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