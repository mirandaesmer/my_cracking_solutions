from unittest import TestCase

from binary_search_tree_node import BinarySearchTreeNode
from chapter_four import ChapterFour


class ChapterFourTests(TestCase):
	def setUp(self):
		self.ch4 = ChapterFour()
		self.unsorted_array = [5, 2, 8, 1, 6, 9]
		self.sorted_array = [1, 2, 5, 6, 8, 9]
		
	def test_problem5(self) -> None:
		# create binary search tree with unsorted array
		bst_root = BinarySearchTreeNode(self.unsorted_array[0])
		_ = [bst_root.insert(i) for i in self.unsorted_array]
		
		# should return sorted list
		nodes = []
		bst_root.in_order_traverse(nodes)
		self.assertEqual(nodes, self.sorted_array)
		
		# intentionally create broken binary tree
		bad_root = BinarySearchTreeNode(self.unsorted_array[0])
		bad_root.left = BinarySearchTreeNode(7)
		bad_root.right = BinarySearchTreeNode(3)
		_ = [bad_root.insert(i) for i in self.unsorted_array]
		
		# should return UNSORTED list
		nodes = []
		bad_root.in_order_traverse(nodes)
		self.assertEqual(nodes, [1, 2, 7, 5, 3, 6, 8, 9])
		
		# test positive and negative cases
		self.assertTrue(self.ch4.problem5(bst_root))
		self.assertFalse(self.ch4.problem5(bad_root))
