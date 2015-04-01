# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		new_list = []
		new_list.extend(A)
		new_list.extend(B)
		new_list.sort()
		median = 0
		if len(new_list)%2 == 0:
			median = float((float(new_list[len(new_list)/2] + new_list[(len(new_list)/2)-1]))/2)
		else:
			median = new_list[len(new_list)/2]
		return median
