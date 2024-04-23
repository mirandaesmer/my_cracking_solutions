from __future__ import annotations
from typing import Optional, List


class BinaryTreeNode:
    def __init__(self, data: int = None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, new_data: int) -> None:
        # default insert per level if not specified
        if self.data is None:
            self.data = new_data
        elif self.left is None:
            self.left = BinaryTreeNode(new_data)
        elif self.right is None:
            self.right = BinaryTreeNode(new_data)
        else:  # has both left and right
            
            # only insert right if right nodes are empty
            has_full_left = (self.left.left is not None and
                             self.left.right is not None)
            if has_full_left:
                self.right.insert(new_data)
            else:
                self.left.insert(new_data)

    def find(self, search_data: int) -> Optional[BinaryTreeNode]:
        if self.data is not None:
            if search_data == self.data:
                return self
        
        left_search = None
        if self.left is not None:
            left_search = self.left.find(search_data)
        if left_search is not None:
            return left_search
        
        right_search = None
        if self.right is not None:
            right_search = self.right.find(search_data)
        if right_search is not None:
            return right_search

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
        
    def get_path_to_node(
            self,
            node: BinaryTreeNode,
            target: BinaryTreeNode,
    ) -> Optional[List[BinaryTreeNode]]:
        # Base cases
        if not node:
            return []
        if node == target:
            return [node]
        
        # Will only return if node is found
        path = self.get_path_to_node(node.left, target)
        if path:
            return [node] + path
        
        # Right branch
        path = self.get_path_to_node(node.right, target)
        if path:
            return [node] + path
        
        # False on default
        return []
