#  Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.

# click to show clarification.
# Clarification:

#     What constitutes a word?
#     A sequence of non-space characters constitutes a word.

#     Could the input string contain leading or trailing spaces?
#     Yes. However, your reversed string should not contain leading or trailing spaces.

#     How about multiple spaces between two words?
#     Reduce them to a single space in the reversed string.

class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		temp = s[:].strip().replace("  ", " ")
		new_str = temp.split(" ")
		no_space_list = []
		for i in range(len(new_str)):
			if new_str[i].strip() != "":
				no_space_list.append(new_str[i])
		reversed_str = no_space_list[-1:-len(no_space_list)-1:-1]
		return " ".join(reversed_str)
