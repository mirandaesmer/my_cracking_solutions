from unittest import TestCase

from random_binary_tree_node import RandomBinaryTree


class MyTestCase(TestCase):
    def setUp(self):
        self.rbt = RandomBinaryTree()
    
    def test_insert(self):
        self.rbt.insert(0)
        self.rbt.insert(1)  # left
        self.rbt.insert(2)  # right
        
        self.assertEqual(self.rbt._data_list, [0, 1, 2])
        self.assertEqual(self.rbt.root.data, 0)
        self.assertEqual(self.rbt.root.left.data, 1)
        self.assertEqual(self.rbt.root.right.data, 2)
        
    def test_delete(self):
        # TODO
        pass
    
    def test_get_random_node(self):
        for i in range(7):
            self.rbt.insert(i)
    
        counts = [0] * 7
        for _ in range(1000):
            x = self.rbt.get_random_node()
            counts[x.data] += 1
            
        # Manually check distribution of numbers
        # NOTE, There may be a better way to test this
        print(counts)
