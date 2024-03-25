from unittest import TestCase

from chapter_two import ChapterTwo
from linked_list_node import LinkedListNode


class ChapterTwoTests(TestCase):
    def setUp(self):
        self.ch2 = ChapterTwo()
    
    def test_problem1(self) -> None:
        root = LinkedListNode()
        
        arr = [3, 1, 5, 7, 1, 9, 5, 4]
        for i in arr:
            root.insert(i)
        _ = self.ch2.problem1(root)
        
        data_list = [root.data]
        node = root
        while node.next is not None:
            data_list.append(node.next.data)
            node = node.next
            
        self.assertEqual(data_list, [3, 1, 5, 7, 9, 4])
    
    def test_problem2(self) -> None:
        root = LinkedListNode()
        for i in range(0, 10):
            root.insert(i)
        
        node = self.ch2.problem2(root, 2)
        self.assertEqual(node.data, 7)
        
        node = self.ch2.problem2(root, 5)
        self.assertEqual(node.data, 4)
        
        node = self.ch2.problem2(root, 11)
        self.assertIsNone(node)
    
    def test_problem6(self) -> None:
        non_palin_arr = [1, 5, 7, 7, 4, 1, 5]
        palin_arr = [1, 4, 8, 3, 8, 4, 1]
        non_palin_root = LinkedListNode()
        palin_root = LinkedListNode()
        
        for i in non_palin_arr:
            non_palin_root.insert(i)
        
        for i in palin_arr:
            palin_root.insert(i)
            
        self.assertFalse(self.ch2.problem6(non_palin_root))
        self.assertTrue(self.ch2.problem6(palin_root))

    def test_problem8(self) -> None:
        root = LinkedListNode()
        for i in range(0, 10):
            root.insert(i)
        
        last_node = root
        while last_node.next is not None:
            last_node = last_node.next
        
        # create a loop from last to third node
        third_node = root.next.next.next
        last_node.next = third_node
        self.assertEqual(self.ch2.problem8(root).data, third_node.data)
