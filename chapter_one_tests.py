from unittest import TestCase

from chapter_one import ChapterOne


class ChapterOneTests(TestCase):
    def setUp(self):
        self.ch1 = ChapterOne()
        
    def test_problem1(self):
        self.assertTrue(  # Is unique
            self.ch1.problem1("abcdefghi"),
        )
        self.assertFalse(
            self.ch1.problem1("is not unique"),
        )
        
    def test_problem2(self):
        self.assertTrue(
            self.ch1.problem2("abcde", "ebdac")
        )
        self.assertFalse(
            self.ch1.problem2("abcdxe", "ebdacr")
        )
