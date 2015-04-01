# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

class Solution:
	# @param num, a list of integer
	# @return an integer
	def maximumGap(self, num):
		temp = num[:]
		if len(temp) < 2:
			return 0
		else:
			temp.sort()
			max_gap = []
			for i in range(len(temp)):
				if (i+1) < len(temp):
					max_gap.append(abs(temp[i]-temp[i+1]))
			max_gap.sort()
			return max_gap[len(max_gap)-1]
