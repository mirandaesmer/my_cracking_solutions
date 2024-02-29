from __future__ import annotations
from typing import Optional, List


class BinarySearchTreeNode:
	def __init__(self, data: int = None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	
	def insert(self, new_data: int) -> None:
		if self.data is None:
			self.data = new_data
			
		elif new_data < self.data:
			if self.left is None:
				self.left = BinarySearchTreeNode(new_data)
			else:
				self.left.insert(new_data)
		
		elif new_data > self.data:
			if self.right is None:
				self.right = BinarySearchTreeNode(new_data)
			else:
				self.right.insert(new_data)

	def find(self, search_data: int) -> Optional[BinarySearchTreeNode]:
		if self.data is None:
			return None
		if self.data == search_data:
			return self
		
		if search_data < self.data:
			if self.left is None:
				return None
			else:
				return self.left.find(search_data)
			
		if search_data > self.data:
			if self.right is None:
				return None
			else:
				return self.right.find(search_data)

	def in_order_traverse(self, node_list: List) -> None:
		if self.left is not None:
			self.left.in_order_traverse(node_list)
		
		node_list.append(self.data)
		
		if self.right is not None:
			self.right.in_order_traverse(node_list)
	
	def pre_order_traverse(self, node_list: List) -> None:
		node_list.append(self.data)
		
		if self.left is not None:
			self.left.pre_order_traverse(node_list)
		
		if self.right is not None:
			self.right.pre_order_traverse(node_list)
	
	def post_order_traverse(self, node_list: List) -> None:
		if self.left is not None:
			self.left.post_order_traverse(node_list)
		
		if self.right is not None:
			self.right.post_order_traverse(node_list)
			
		node_list.append(self.data)