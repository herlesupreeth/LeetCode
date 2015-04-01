# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
	# @param num, a list of integers
	# @return an integer
	def majorityElement(self, num):
		tempdict = {}
		tempset = set(num)
		for i in tempset:
			tempdict.update({i: num.count(i)})
		temp = sorted(tempdict.items(), key=lambda num: num[1])
		return temp[len(tempdict) -1][0]