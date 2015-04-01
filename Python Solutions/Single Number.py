# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		if not A:
			return None
		else:
			setTemp = set(A)
			setTemp = list(setTemp)
			lenset = len(setTemp)
			tempA = A
			for i in setTemp:
				tempA.remove(i)
			tempB = list(set(setTemp)-set(tempA))
			return tempB[0]