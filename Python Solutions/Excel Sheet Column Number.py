# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

class Solution:
	# @param s, a string
	# @return an integer
	def titleToNumber(self, s):
		alphastr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		alphadict = {}
		for i in range(0,len(alphastr)):
			alphadict[alphastr[i]] = i+1
		temp = 0
		m = len(s)
		for i in range(0,len(s)-1):
			temp += (alphadict[s[i]]) * (26**(m-1))
			m -= 1
		temp += alphadict[s[len(s)-1]]
		return temp