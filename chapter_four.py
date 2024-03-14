from typing import List

from binary_search_tree_node import BinarySearchTreeNode
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
