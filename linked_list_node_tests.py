import unittest

from linked_list_node import LinkedListNode


class LinkedListTests(unittest.TestCase):
    def test_insert(self) -> None:
        node = LinkedListNode(0)
        
        for i in range(1,10):
            node.insert(i)
        
        for j in range(0, 10):
            self.assertEqual(node.data, j)
            node = node.next
        self.assertIsNone(node)  # last node reached
