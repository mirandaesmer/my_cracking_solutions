from unittest import TestCase

from two_stack_queue import TwoStackQueue


class MyTestCase(TestCase):
    def setUp(self):
        self.tsq = TwoStackQueue()
        
    def test_push(self):
        for i in range(5):
            self.tsq.push(i)
        
        # should be FIFO
        self.assertEqual(self.tsq._data_stack, list(range(5)))

    def test_pop(self):
        # push 5
        for i in range(5):
            self.tsq.push(i)
            
        # pop 2
        self.assertEqual(self.tsq.pop(), 0)
        self.assertEqual(self.tsq.pop(), 1)
        
        # push 5 more
        for i in range(5):
            self.tsq.push(i + 5)
        
        # pop 2 others, still FIFO
        self.assertEqual(self.tsq.pop(), 2)
        self.assertEqual(self.tsq.pop(), 3)
        