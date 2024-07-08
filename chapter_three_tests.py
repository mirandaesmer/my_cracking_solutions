from unittest import TestCase

from chapter_three import ChapterThree


class ChapterThreeTests(TestCase):
    def setUp(self):
        self.ch3 = ChapterThree()
        
    def test_problem5(self):
        arr_stack = [3, 2, 5, 1, 4]
        expected_result = [5, 4, 3, 2, 1]
        result = self.ch3.problem5(arr_stack)
        self.assertEqual(result, expected_result)
