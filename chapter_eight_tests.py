from unittest import TestCase

from chapter_eight import ChapterEight


class ChapterEightTests(TestCase):
    def setUp(self):
        self.ch8 = ChapterEight()
        
    def test_problem_5(self):
        self.assertEqual(self.ch8.problem5(3, 4), 12)
        self.assertEqual(self.ch8.problem5(10, 10), 100)
        self.assertEqual(self.ch8.problem5(6, 8), 48)
        self.assertEqual(self.ch8.problem5(0, 0), 0)