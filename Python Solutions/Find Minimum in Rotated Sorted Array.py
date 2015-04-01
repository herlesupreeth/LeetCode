# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.

class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		temp = num[:]
		temp.sort()
		return temp[0]