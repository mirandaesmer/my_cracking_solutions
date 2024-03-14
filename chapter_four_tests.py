from unittest import TestCase

from binary_search_tree_node import BinarySearchTreeNode
from chapter_four import ChapterFour
from directed_graph import DirectedGraph, GraphNode


class ChapterFourTests(TestCase):
    def setUp(self):
        self.ch4 = ChapterFour()
        self.unsorted_array = [5, 2, 8, 1, 6, 9]
        self.sorted_array = [1, 2, 5, 6, 8, 9]
    
    def test_problem1(self) -> None:
        dg = DirectedGraph()
        nodes = [GraphNode(i, set()) for i in range(0, 10)]
        for n in nodes:
            dg.add_node(n)
            
        # create directed graph w/ these adj map:
        exp_adjacency_map = {
            0: {7},     # nothing points to 0
            1: {2, 3},
            2: {4, 5},
            3: {6},
            4: {2, 7},  # (2-4 is a loop)
            5: set(),
            6: {8},
            7: set(),
            8: {3},     # (3-6-8 is a loop)
            9: set(),   # isolated node
        }
        
        dg.add_connection(nodes[1], nodes[2])
        dg.add_connection(nodes[1], nodes[3])
        dg.add_connection(nodes[2], nodes[4])
        dg.add_connection(nodes[2], nodes[5])
        dg.add_connection(nodes[3], nodes[6])
        dg.add_connection(nodes[4], nodes[7])
        dg.add_connection(nodes[4], nodes[2])
        dg.add_connection(nodes[6], nodes[8])
        dg.add_connection(nodes[8], nodes[3])
        dg.add_connection(nodes[0], nodes[7])
        
        self.assertEqual(dg._adjacency_map, exp_adjacency_map)
        
        # false cases
        self.assertFalse(self.ch4.problem1(dg, nodes[9], nodes[2]))
        self.assertFalse(self.ch4.problem1(dg, nodes[1], nodes[9]))
        
        # forwards match (a to b)
        self.assertTrue(self.ch4.problem1(dg, nodes[1], nodes[8]))
        self.assertTrue(self.ch4.problem1(dg, nodes[1], nodes[8]))
        
        # back match (b to a)
        self.assertTrue(self.ch4.problem1(dg, nodes[4], nodes[2]))
        self.assertTrue(self.ch4.problem1(dg, nodes[6], nodes[3]))

    def test_problem3(self) -> None:
        # TEST BST:
        #        5
        #     2    8
        #   1     6  9
        bst_root = BinarySearchTreeNode(5)  # LVL 1
        
        bst_root.insert(2)  # LVL 2
        bst_root.insert(8)
        
        bst_root.insert(1)  # LVL 3
        bst_root.insert(6)
        bst_root.insert(9)
        
        levels = self.ch4.problem3(bst_root)
        first, second, third = levels
        
        self.assertEqual(first.data, 5)
        self.assertEqual(second.data, 2)
        self.assertEqual(second.next.data, 8)
        self.assertEqual(third.data, 1)
        self.assertEqual(third.next.data, 6)
        self.assertEqual(third.next.next.data, 9)
        
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

    def test_problem6(self) -> None:
        root = BinarySearchTreeNode(5)
        root.insert(2)
        root.insert(8)
        root.insert(1)
        root.insert(6)
        root.insert(9)
        
        self.assertEqual(self.ch4.problem6(root, 1), 2)
        self.assertEqual(self.ch4.problem6(root, 2), 5)
        self.assertEqual(self.ch4.problem6(root, 5), 6)
        self.assertEqual(self.ch4.problem6(root, 6), 8)
        self.assertIsNone(self.ch4.problem6(root, 9))
