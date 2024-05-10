from unittest import TestCase

from chapter_eight import ChapterEight


class ChapterEightTests(TestCase):
    def setUp(self):
        self.ch8 = ChapterEight()
    
    def test_problem_1(self):
        self.assertEqual(self.ch8.problem1(1), 1)
        self.assertEqual(self.ch8.problem1(2), 2)
        self.assertEqual(self.ch8.problem1(3), 4)
        self.assertEqual(self.ch8.problem1(10), 274)
    
    def test_problem_4(self):
        res = self.ch8.problem4({1, 2, 3, 4})
        expected = [
            {1}, {2}, {3}, {4},
            {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4},
            {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
            {1, 2, 3, 4}
        ]
        self.assertEqual(res, expected)
        
    def test_problem_5(self):
        self.assertEqual(self.ch8.problem5(3, 4), 12)
        self.assertEqual(self.ch8.problem5(10, 10), 100)
        self.assertEqual(self.ch8.problem5(6, 8), 48)
        self.assertEqual(self.ch8.problem5(0, 0), 0)