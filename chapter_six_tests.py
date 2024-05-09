from unittest import TestCase

from chapter_six import ChapterSix


class ChapterSixTests(TestCase):
    def setUp(self):
        self.ch6 = ChapterSix()
    
    def test_problem6(self):
        # Chapter 6 requires different testing
        print(self.ch6.problem6())
