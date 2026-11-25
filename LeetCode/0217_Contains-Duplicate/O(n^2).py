""" 217. Contains Duplicate
Author: Mrunal Nirajkumar Shah
Date  : November 13, 2026

Time Complexity : O(n^2)
Space Complexity: O(1)

Method: For ith index and value, I will check its jth indices which are bigger than ith index, 
        and see if the values match with the ith index value.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
    
def main():
    list_nums = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2]
    ]

    list_output = [
        True,
        False,
        True
    ]

    solution = Solution()

    results = []
    for nums in list_nums:
        results.append(solution.containsDuplicate(nums))

    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()