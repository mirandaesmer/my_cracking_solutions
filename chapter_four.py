from typing import List, Optional

from binary_search_tree_node import BinarySearchTreeNode
from binary_tree_node import BinaryTreeNode
from directed_graph import DirectedGraph, GraphNode
from linked_list_node import LinkedListNode


class ChapterFour:
    def problem1(self, dg: DirectedGraph, a: GraphNode, b: GraphNode) -> bool:
        # Route Between Nodes: Given a directed graph, design an algorithm to
        # find out whether there is a route between two nodes.
        a_to_b = dg.bfs(a, b.data)
        b_to_a = dg.bfs(b, a.data)
        
        if a_to_b is None and b_to_a is None:
            return False
        return True
    
    def problem2(self, arr):
        # Given a sorted (increasing order) array with unique integer elements,
        # write an algorithm to create a binary search tree with minimal height
        pass
    
    def problem3(self, root: BinarySearchTreeNode) -> List[LinkedListNode]:
        # Given a binary tree, design an algorithm which creates a linked list
        # of all the nodes at each depth (e.g., if you have a tree with depth
        # D, you'll have D linked lists.
        
        # Breadth-first traversal of the BST
        linked_list_by_level = []
        nodes_at_level = [root]
        
        while True:
            level_data = [
                n.data for n in nodes_at_level if hasattr(n, 'data') and n.data is not None
            ]
            if not level_data:
                break
            
            # Add all node data per level
            root_node = LinkedListNode()
            for d in level_data:
                root_node.insert(d)
            linked_list_by_level.append(root_node)
            
            # Traverse left to right in order
            nodes_temp = []
            for n in nodes_at_level:
                if n.left is not None:
                    nodes_temp.append(n.left)
                
                if n.right is not None:
                    nodes_temp.append(n.right)
            
            if not nodes_temp:
                break
            nodes_at_level = nodes_temp
            
        return linked_list_by_level

    def problem5(self, root: BinarySearchTreeNode) -> bool:
        # Implement a function to check if a binary tree is a binary search
        # tree.
        nodes = []
        root.in_order_traverse(nodes)
        return nodes == sorted(nodes)

    def _get_max_depth(self, node: BinaryTreeNode, level: int) -> int:
        if node is None:
            return level
        if node.left is None and node.right is None:
            return level + 1
        if node.right is None:
            return self._get_max_depth(node.left, level + 1)
        if node.left is None:
            return self._get_max_depth(node.right, level + 1)
        return max(
            self._get_max_depth(node.left, level + 1),
            self._get_max_depth(node.right, level + 1),
        )

    def problem4(self, bt_root: BinaryTreeNode) -> bool:
        # Implement a function to check if a binary tree is balanced. For the
        # purposes of this question, a balanced tree is defined to be a tree
        # such that the heights of the two subtrees of any node never differ
        # by more than one.
        lh = self._get_max_depth(bt_root.left, 1)
        rh = self._get_max_depth(bt_root.right, 1)
        
        if max(rh, lh) - min(rh, lh) > 1:
            return False
        return True
    
    def problem6(self, root: BinarySearchTreeNode, precessor_data: int) -> Optional[int]:
        # Write an algorithm to find the "next" node (i.e., in-order successor)
        # of a given node in a binary search tree. You may assume that each
        # node has a link to its parent.
        
        # in this case, only returning data
        in_order_data = []
        root.in_order_traverse(in_order_data)
        if not in_order_data:
            return None
        if precessor_data not in in_order_data:
            return None
        if in_order_data[-1] == precessor_data:
            return None
        
        idx = in_order_data.index(precessor_data)
        return in_order_data[idx + 1]
