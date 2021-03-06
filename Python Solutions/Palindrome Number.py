# Determine whether an integer is a palindrome. Do this without extra space.

# click to show spoilers.
# Some hints:

# Could negative integers be palindromes? (ie, -1)

# If you are thinking of converting the integer to string, note the restriction of using extra space.

# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

# There is a more generic way of solving this problem.

class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		temp = abs(x)
		m = ""
		while temp != 0:
			m += str(temp%10)
			temp = temp/10
		if m == m[::-1] and (x >= 0):
			return True
		return False