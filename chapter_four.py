from typing import Optional

from binary_search_tree_node import BinarySearchTreeNode
from linked_list_node import LinkedListNode


class ChapterFour:
    def problem2(self, arr):
        # Given a sorted (increasing order) array with unique integer elements,
        # write an algorithm to create a binary search tree with minimal height
        pass
    
    def problem3(self, root: BinarySearchTreeNode) -> Optional[LinkedListNode]:
        # Given a binary tree, design an algorithm which creates a linked list
        # of all the nodes at each depth (e.g., if you have a tree with depth
        # D, you'll have D linked lists.
        
        # TODO WIP
        pass
    
    def problem5(self, root: BinarySearchTreeNode) -> bool:
        # Implement a function to check if a binary tree is a binary search
        # tree.
        nodes = []
        root.in_order_traverse(nodes)
        return nodes == sorted(nodes)
