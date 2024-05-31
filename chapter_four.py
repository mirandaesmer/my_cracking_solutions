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

    def midpt_traverse(self, arr: List[int]) -> List[int]:
        if not arr:  # Empty case
            return []
        
        arr_size = len(arr)
        if len(arr) == 1:
            return arr
        
        mid = arr_size // 2
        
        # pre-order traversal
        l = arr[:mid]
        midpt = arr[mid]
        r = arr[mid + 1:]
        
        return [midpt] + self.midpt_traverse(l) + self.midpt_traverse(r)

    def problem2(self, sorted_arr: List[int]) -> Optional[BinarySearchTreeNode]:
        # Given a sorted (increasing order) array with unique integer elements,
        # write an algorithm to create a binary search tree with minimal height
        
        # Complexity: O( n^2 ) since slicing in python is O( k ) where k is the
        # size of the slice.
        bst_sorted_arr = self.midpt_traverse(sorted_arr)
        
        if not bst_sorted_arr:
            return None
        
        bts_root = BinarySearchTreeNode(bst_sorted_arr[0])
        for i in bst_sorted_arr[1:]:
            bts_root.insert(i)
        
        return bts_root

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

    def problem5(self, root: BinarySearchTreeNode) -> bool:
        # Implement a function to check if a binary tree is a binary search
        # tree.
        nodes = []
        root.in_order_traverse(nodes)
        return nodes == sorted(nodes)
    
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
    
    def problem8(
            self,
            root: BinaryTreeNode,
            node_a: BinaryTreeNode,
            node_b: BinaryTreeNode,
    ) -> Optional[BinaryTreeNode]:
        # Design an algorithm and write code to find the first common ancestor
        # of two nodes in a binary tree. Avoid storing additional nodes in a
        # data structure. NOTE: This is not necessarily a binary search tree.
        
        # NOTE: Does not avoid storing additional nodes
        root_to_a = root.get_path_to_node(root, node_a)
        root_to_b = root.get_path_to_node(root, node_b)
        
        if not root_to_a or not root_to_b:
            return None
        
        # If there are paths, there must be at least 1 shared
        ancestor = root
        for i in range(min(len(root_to_a), len(root_to_b))):
            if root_to_a[i] != root_to_b[i]:
                return ancestor
            ancestor = root_to_a[i]
    
    def _search_node(
            self,
            t1_node: BinaryTreeNode,
            search_node: BinaryTreeNode
    ) -> bool:
        # Traversal can vary depending on problem details, using pre-order here
        node = t1_node
        if node.data is not None and node == search_node:
            return True
        
        if node.left is not None:
            return self._search_node(node.left, search_node)
        if node.right is not None:
            return self._search_node(node.right, search_node)
        
    def problem10(
            self,
            t1_root: BinaryTreeNode,
            t2_root: BinaryTreeNode,
    ) -> bool:
        # T1 and T2 are two very large binary trees, with T1 much bigger than
        # T2. Create an algorithm to determine if T2 is a subtree of T1. A tree
        # T2 is a subtree of T1 if there exists a node n in T1 such that the
        # subtree of n is identical to T2. That is, if you cut off the tree at
        # node n, the two trees would be identical.
        result = self._search_node(t1_root, t2_root)
        if result is None:
            return False
        return True
    
    def problem11(self):
        # You are implementing a binary tree class from scratch which, in
        # addition to insert, find, and delete, has a method getRandomNode()
        # which returns a random node from the tree. All nodes should be
        # equally likely to be chosen. Design and implement an algorithm for
        # getRandomNode, and explain how you would implement the rest of the
        # methods.
        
        # NOTE: see random_binary_tree_node.py and
        # random_binary_tree_node_tests.py
        pass
