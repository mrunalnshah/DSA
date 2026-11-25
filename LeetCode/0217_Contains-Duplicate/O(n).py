""" 217. Contains Duplicate
Author: Mrunal Nirajkumar Shah
Date  : November 13, 2026

Time Complexity : O(n)
Space Complexity: O(n)

Method: Build a hash_map and check if the value of ith index is in hash_map, 
        if not add that value in hash_map. if the value is already in hash_map, return True.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                return True

            hash_map[num] = 1

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