from unittest import TestCase

from min_stack import MinStack


class MinStackTests(TestCase):
    def setUp(self):
        self.ms = MinStack()
        
    def test_push(self):
        self.ms.push(4)
        self.ms.push(5)
        self.ms.push(6)
        self.assertEqual(self.ms._stack_list, [4, 5, 6])

    def test_pop(self):
        self.ms.push(4)
        self.ms.push(5)
        self.ms.push(6)
        
        popped_data = [self.ms.pop() for _ in range(3)]
        self.assertEqual(popped_data, [6, 5, 4])
        
        # Pop on empty
        with self.assertRaises(Exception):
            self.ms.pop()
            
    def test_min(self):
        minimum = self.ms.min()
        self.assertIsNone(minimum)
        
        self.ms.push(5)
        minimum = self.ms.min()
        self.assertEqual(minimum, 5)
        
        self.ms.push(6)
        self.ms.push(3)
        self.ms.push(8)
        minimum = self.ms.min()
        self.assertEqual(minimum, 3)
        
        # pop 3 out, min should revert to 5
        self.ms.pop()
        self.ms.pop()
        minimum = self.ms.min()
        self.assertEqual(minimum, 5)
