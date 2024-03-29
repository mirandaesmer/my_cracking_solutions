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
        # unused for now
        pass

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