"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9 Output: [0,1] Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6 Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6 Output: [0,1]



Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

# solution 1
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]

# Runtime: 4044 ms, faster than 17.77% of Python online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 24.31% of Python online submissions for Two Sum.

# solution 2
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, v in enumerate(nums):
            if target - v not in dict:
                dict[v] = i
            else:
                return [dict[target-v], i]

# Runtime: 36 ms, faster than 98.74% of Python online submissions for Two Sum.
# Memory Usage: 14.1 MB, less than 90.58% of Python online submissions for Two Sum.