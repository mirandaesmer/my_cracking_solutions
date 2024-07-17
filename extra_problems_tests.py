from unittest import TestCase

from extra_problems import ExtraProblems
from linked_list_node import LinkedListNode


class ExtraProblemsTests(TestCase):
    def setUp(self):
        self.ex = ExtraProblems()
        
    def test_problem1(self):
        # Input: lists = [[1,4,5],[1,3,4],[2,6]]
        # Output: [1,1,2,3,4,4,5,6]
        root_a = LinkedListNode()
        root_a.insert(1)
        root_a.insert(4)
        root_a.insert(5)
        
        root_b = LinkedListNode()
        root_b.insert(1)
        root_b.insert(3)
        root_b.insert(4)
        
        root_c = LinkedListNode()
        root_c.insert(2)
        root_c.insert(6)
        
        result = self.ex.problem1([root_a, root_b, root_c])
        self.assertIsNotNone(result.data)
        
        # convert to list to compare
        sorted_list = []
        while result is not None:
            sorted_list.append(result.data)
            result = result.next
            
        self.assertEqual(sorted_list, [1, 1, 2, 3, 4, 4, 5, 6])

    def test_problem2(self):
        grid_a = [  # 1
          [1,1,1,1,0],
          [1,1,0,1,0],
          [1,1,0,0,0],
          [0,0,0,0,0]
        ]
        grid_b = [  # 3
          [1,1,0,0,0],
          [1,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,1]
        ]
        self.assertEqual(self.ex.problem2(grid_a), 1)
        self.assertEqual(self.ex.problem2(grid_b), 3)
