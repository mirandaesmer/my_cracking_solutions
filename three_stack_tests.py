from unittest import TestCase

from three_stack import ThreeStack


class ThreeStackTests(TestCase):
    def setUp(self):
        self.ts = ThreeStack()
        
        self.ts.push_on_stack(11, 1)
        self.ts.push_on_stack(12, 1)
        self.ts.push_on_stack(13, 1)
        
        self.ts.push_on_stack(21, 2)
        self.ts.push_on_stack(22, 2)
        self.ts.push_on_stack(23, 2)
        
        self.ts.push_on_stack(31, 3)
        self.ts.push_on_stack(32, 3)
        self.ts.push_on_stack(33, 3)
    
    def test_push_on_stack(self):
        # Expected data, see setUp()
        # 1: [11, 12, 13]
        # 2: [21, 22, 23]
        # 3: [31, 32, 33]
        
        # Single array repr:
        exp_arr_data = [11, 21, 31, 12, 22, 32, 13, 23, 33]
        actual_data = [i for i in self.ts._array if i is not None]
        self.assertEqual(actual_data, exp_arr_data)

    def test_pop_from_stack(self):
        # Pop 1 from second
        pop_val = self.ts.pop_from_stack(2)
        self.assertEqual(pop_val, 23)
        
        # Pop all from 1st and test exception
        pop_val = [self.ts.pop_from_stack(1) for _ in range(3)]
        self.assertEqual(pop_val, [13, 12, 11])
        with self.assertRaises(Exception):
            self.ts.pop_from_stack(1)
        
        # Pop 1 from 3, then add 2, then pop
        pop_val = self.ts.pop_from_stack(3)
        self.assertEqual(pop_val, 33)
        
        self.ts.push_on_stack(88, 3)
        self.ts.push_on_stack(99, 3)
        pop_val = self.ts.pop_from_stack(3)
        self.assertEqual(pop_val, 99)
        
        # Contains None because array 3 index is higher than others
        exp_arr_data = [11, 21, 31, 12, 22, 32, 13, 23, 88, None, None, 99]
        actual_data = self.ts._array[:12]
        self.assertEqual(actual_data, exp_arr_data)
