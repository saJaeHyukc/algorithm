"""
Given the array of integers nums, 
you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

"""
from typing import List

# my case - sort
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1) 
    
    
# other case - max, remove
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums.remove(first_max)
        second_max = max(nums)
        product = (first_max - 1) * (second_max-1)
        return product
    
# other case - for loop
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for i in range(0,len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]
        return (max1-1)*(max2-1)