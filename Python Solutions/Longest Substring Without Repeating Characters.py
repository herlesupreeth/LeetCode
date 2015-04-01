# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		tempString = []
		lenString = {}
		if s == "":
			return 0
		for j in range(0, len(s)):
			if s[j] in tempString:
				lenString[('').join(tempString)] = len(('').join(tempString))
				tempString = tempString[tempString.index(s[j])+1:len(tempString)]
				tempString.append(s[j])
			else:
				tempString.append(s[j])
			if j == len(s) - 1:
				lenString[('').join(tempString)] = len(('').join(tempString))
		if len(lenString) == 0:
			return 0
		return max(sorted(i for i in lenString.values()))
