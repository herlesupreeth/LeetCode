# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		if numRows == 0:
			return []
		elif numRows == 1:
			return [[1]]
		elif numRows == 2:
			return [[1],[1,1]]
		else:
			result = [[1],[1,1]]
			for i in range(2,numRows):
				temp = []
				for j in range(0,len(result[i-1])-1):
					temp.append(result[i-1][j] + result[i-1][j+1])
				temp.insert(0,1)
				temp.append(1)
				result.append(temp)
			return result
