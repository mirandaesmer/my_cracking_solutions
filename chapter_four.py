from binary_search_tree_node import BinarySearchTreeNode


class ChapterFour:
	def problem2(self, arr):
		# Given a sorted (increasing order) array with unique integer elements,
		# write an algorithm to create a binary search tree with minimal height
		pass
	
	def problem5(self, root: BinarySearchTreeNode) -> bool:
		# Implement a function to check if a binary tree is a binary search tree.
		nodes = []
		root.in_order_traverse(nodes)
		return nodes == sorted(nodes)
