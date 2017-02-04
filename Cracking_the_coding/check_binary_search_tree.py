""" Node is defined as"""
from collections import deque,defaultdict
import copy

tree_q = deque()
tree_dict = defaultdict()

class node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.gt = -2
		self.lt = 10001

	def check_subtree(self, parent, f):	
		self.lt = parent.lt
		self.gt = parent.gt
		if not f:
			if parent.data < self.lt:
				self.lt = parent.data
		else:
			if parent.data > self.gt:
				self.gt = parent.data
		return self.data > self.gt and self.data < self.lt	

def insert_queue(node, f):
	global tree_q
	global tree_dict
	if f:
		data = 10001
	else:
		data = -2
	if node:
		tree_q.appendleft(node)
		data = node.data
		if tree_dict.get(data):
			return -1
		tree_dict[data] = 1
	return data


def check_binary_search_tree_(root):

	global tree_q
	tree_q.append(root)
	global tree_dict 
	tree_dict[root.data] = 1

	while tree_q:
		temp = tree_q.pop()
		left_data = -1
		right_data = 10000
		left_data = insert_queue(temp.left,0)
		right_data = insert_queue(temp.right, 1)
		if right_data == -1 or left_data == -1:
			return False
		if temp.left:
			if not (temp.left.check_subtree(temp,0)):
				return False
		if temp.right:
			if not temp.right.check_subtree(temp,1):
				return False
	return True



