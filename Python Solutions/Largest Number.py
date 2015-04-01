# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
	# @param num, a list of integers
	# @return a string
	def largestNumber(self, num):
		strList = []
		maxlength = 0
		count = 0
		for i in num:
			strList.append(str(i))
			if i == 0:
				count +=1
		if count == len(num):
			return '0'
		retList = sorted(strList, cmp=lambda x,y: self.compare(x,y), reverse=True)
		return ('').join(retList)

	def compare(self,x,y):
		tempA = x + y
		tempB = y + x
		#print tempB, tempA
		return cmp(tempA,tempB)