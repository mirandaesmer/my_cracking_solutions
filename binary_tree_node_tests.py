from unittest import TestCase

from binary_search_tree_node import BinarySearchTreeNode


class BinaryTreeNodeTests(TestCase):
    def setUp(self):
        self.root = BinarySearchTreeNode(5)
        self.root.insert(2)
        self.root.insert(8)
        
        self.root.insert(1)
        self.root.insert(6)
        self.root.insert(9)
        
    def test_insert(self) -> None:
        self.assertEqual(self.root.data, 5)
        
        left = self.root.left
        self.assertEqual(left.data, 2)
        self.assertEqual(left.left.data, 1)
        
        right = self.root.right
        self.assertEqual(right.data, 8)
        self.assertEqual(right.right.data, 9)
        self.assertEqual(right.left.data, 6)

    def test_find(self) -> None:
        self.assertEqual(self.root.find(5), self.root)
        self.assertEqual(self.root.find(2), self.root.left)
        self.assertEqual(self.root.find(8), self.root.right)
        
        self.assertIsNone(self.root.find(7))
        self.assertIsNone(self.root.find(0))
        self.assertIsNone(self.root.find(22))

    def test_in_order_traverse(self) -> None:
        nodes = []
        self.root.in_order_traverse(nodes)
        self.assertEqual(nodes, [1, 2, 5, 6, 8, 9])

    def test_pre_order_traverse(self) -> None:
        nodes = []
        self.root.pre_order_traverse(nodes)
        self.assertEqual(nodes, [1, 2, 6, 9, 8, 5])
    
    def test_post_order_traverse(self) -> None:
        nodes = []
        self.root.post_order_traverse(nodes)
        self.assertEqual(nodes, [5, 2, 1, 8, 6, 9])
