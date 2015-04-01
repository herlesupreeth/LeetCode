# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		temp = {}
		for i in range(len(num)):
			temp.update({i+1:num[i]})
		sorted_temp = sorted(temp.items(), key=lambda x: x[1])
		for i in range(len(sorted_temp)):
			for j in range(len(sorted_temp)):
				if i != j and sorted_temp[i][1]+sorted_temp[j][1] == target:
					if (sorted_temp[i][0]<sorted_temp[j][0]):
						return (sorted_temp[i][0], sorted_temp[j][0])
					else:
						return (sorted_temp[j][0], sorted_temp[i][0])