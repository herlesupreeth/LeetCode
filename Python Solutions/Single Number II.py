# Given an array of integers, every element appears three times except for one. Find that single one.

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
			for i in range(len(setTemp)):
				if A.count(setTemp[i]) < 3:
					return setTemp[i]
				if A.count(setTemp[len(setTemp)-1-i]) < 3:
					return setTemp[len(setTemp)-1-i]
			return None