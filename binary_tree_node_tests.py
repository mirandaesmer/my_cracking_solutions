from unittest import TestCase

from binary_tree_node import BinaryTreeNode


class BinaryTreeNodeTests(TestCase):
    def setUp(self):
        # should fill out evenly
        self.root = BinaryTreeNode(1)
        
        self.root.insert(11)
        self.root.insert(12)
        
        self.root.insert(21)
        self.root.insert(22)
        self.root.insert(23)
        self.root.insert(24)
        
    def test_insert(self) -> None:
        # see setUp()
        self.assertEqual(self.root.data, 1)
        
        self.assertEqual(self.root.left.data, 11)
        self.assertEqual(self.root.right.data, 12)

        self.assertEqual(self.root.left.left.data, 21)
        self.assertEqual(self.root.left.right.data, 22)
        self.assertEqual(self.root.right.left.data, 23)
        self.assertEqual(self.root.right.right.data, 24)

    def test_find(self):
        result = self.root.find(30)
        self.assertIsNone(result)
        
        result = self.root.find(40)
        self.assertIsNone(result)
        
        result = self.root.find(100)
        self.assertIsNone(result)
        
        # at root
        result = self.root.find(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 1)
        
        # deeper nodes
        result = self.root.find(11)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 11)
        
        result = self.root.find(24)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 24)
