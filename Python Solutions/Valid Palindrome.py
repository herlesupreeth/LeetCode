# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome. 

class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		if not s:
			return True
		else:
			tempString = []
			alpharange = range(ord('a'), ord('z')+1) + range(ord('0'), ord('9')+1)
			for i in s:
				if ord(i.lower()) in alpharange:
					tempString.append(i.lower())
			if tempString == tempString[::-1]:
				return True
			else:
				return False