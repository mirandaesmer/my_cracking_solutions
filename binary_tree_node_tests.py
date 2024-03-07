from unittest import TestCase

from binary_tree_node import BinaryTreeNode


class BinaryTreeNodeTests(TestCase):
    def test_insert(self) -> None:
        # should fill out evenly
        self.root = BinaryTreeNode(1)
        
        self.root.insert(11)
        self.root.insert(12)
        
        self.root.insert(21)
        self.root.insert(22)
        self.root.insert(23)
        self.root.insert(24)
        
        self.assertEqual(self.root.data, 1)
        
        self.assertEqual(self.root.left.data, 11)
        self.assertEqual(self.root.right.data, 12)

        self.assertEqual(self.root.left.left.data, 21)
        self.assertEqual(self.root.left.right.data, 22)
        self.assertEqual(self.root.right.left.data, 23)
        self.assertEqual(self.root.right.right.data, 24)
