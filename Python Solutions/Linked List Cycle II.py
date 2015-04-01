#  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		if head == None:
			return None
		temp = head
		dictHash = {}
		while temp.next != None:
			dictHash[temp] = temp.val
			if dictHash.has_key(temp.next):
				return temp.next
			else:
				temp = temp.next
		return None