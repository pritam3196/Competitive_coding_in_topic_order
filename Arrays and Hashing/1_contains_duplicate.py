"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


Solution Ideas:
We can brute force or we can first sort the array but sorting takes ologn time where n is the 
size of the array. Or we can use extra space in implementing hashset and the time and space 
complexity comes down to O(n)

"""

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		hashset = set()

		for n in nums:
			if n in hashset:
				return True
			hashset.add(n)

		return False


