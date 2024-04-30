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

    def test_problem3(self):
        original = [ch for ch in  " ab ab  ab"]
        expected = [ch for ch in "%20ab%20ab%20%20ab"]
        
        self.assertEqual(self.ch1.problem3(original), expected)

    def test_problem4(self):
        self.assertTrue(
            self.ch1.problem4("TactCoa")
        )
        self.assertTrue(
            self.ch1.problem4("aaaabbb")
        )
        self.assertFalse(
            self.ch1.problem4("12312323")
        )
        self.assertFalse(
            self.ch1.problem4("qwerty")
        )
    
    def test_problem6(self):
        self.assertEqual( # no compression necessary
            self.ch1.problem6('abcdef'),
            'abcdef'
        )
        self.assertEqual(
            self.ch1.problem6('aabcccccaaa'),
            'a2b1c5a3'
        )