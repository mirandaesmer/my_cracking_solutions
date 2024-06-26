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
    
    def test_problem5(self):
        self.assertTrue(self.ch1.problem5('pale', 'ple'))
        self.assertTrue(self.ch1.problem5('pales', 'pale'))
        self.assertTrue(self.ch1.problem5('pale', 'bale'))
        self.assertFalse(self.ch1.problem5('pale', 'bake'))
    
    def test_problem6(self):
        self.assertEqual(  # no compression necessary
            self.ch1.problem6('abcdef'),
            'abcdef'
        )
        self.assertEqual(
            self.ch1.problem6('aabcccccaaa'),
            'a2b1c5a3'
        )
    
    def test_problem8(self):
        base_case1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        base_case2 = [[5, 1], [1, 8]]
        
        self.assertEqual(self.ch1.problem8(base_case1), base_case1)
        self.assertEqual(self.ch1.problem8(base_case2), base_case2)
        
        test_matrix = [
            [1, 2, 3],
            [4, 0, 7],
            [5, 6, 3],
        ]
        exp_matrix = [
            [1, 0, 3],
            [0, 0, 0],
            [5, 0, 3],
        ]
        self.assertEqual(self.ch1.problem8(test_matrix), exp_matrix)
        
        test_matrix = [
            [0, 2, 3],
            [4, 9, 0],
            [5, 6, 3],
        ]
        exp_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 6, 0],
        ]
        self.assertEqual(self.ch1.problem8(test_matrix), exp_matrix)
    
    def test_problem9(self):
        self.assertTrue(self.ch1.problem9('waterbottle', 'erbottlewat'))
        self.assertTrue(self.ch1.problem9('water', 'terwa'))
        
        self.assertFalse(self.ch1.problem9('abcde', 'abdce'))
        self.assertFalse(self.ch1.problem9('1234', '4321'))