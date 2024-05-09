from typing import Tuple, List, Optional


class ChapterSixteen:
    def problem1(self, num_a: int, num_b: int) -> Tuple[int, int]:
        # Write a function to swap a number in place (that is, without temporary
        # variables).
        
        # Complexity: O ( n-m ) where n is the larger number and m the smaller.
        # Python also has built in swap which simply changes refs 'a, b = b, a'
        if num_a > num_b:
            for _ in range(num_a - num_b):
                num_a -= 1
                num_b += 1
        if num_a < num_b:
            for _ in range(num_b - num_a):
                num_a += 1
                num_b -= 1
        return num_a, num_b
    
    def problem2(self, word: str, book: str) -> int:
        # Design a method to find the frequency of occurrences of any given word
        # in a book. What if we were running this algorithm multiple times?
        
        # Complexity: O( n * k ) where n is word length, k is the amount of
        # occurrences of the first letter of the target word in the book. k can
        # be reduced to a constant if slicing is not used.
        occurrences = 0
        word_len = len(word)
        book_len = len(book)
        last_char_to_read = book_len - word_len
        
        for i in range(0, last_char_to_read):
            if book[i] == word[0]:  # limits slicing a bit, can be repeated
                if book[i: i + word_len] == word:
                    occurrences += 1
        return occurrences

    def problem4(self, game: List[List[str]]) -> Optional[str]:
        # Design an algorithm to figure out if someone has won a game of
        # tic-tac-toe.
        
        # Complexity: O ( 9k ) where k is a constant at most the size of the
        # gameboard, worst case scenario is still constant time
        # Assuming board is formatted correctly
        
        # Rows
        for row in game:
            if row[0] == row[1] == row[2]:
                return row[0]
        
        # Diagonals
        if game[0][0] == game[1][1] == game[2][2]:
            return game[0][0]
        if game[0][2] == game[1][1] == game[2][0]:
            return game[0][0]
        
        # Columns
        for i in range(0, 3):
            if game[i][0] == game[i][1] == game[i][2]:
                return game[i][0]
        return None

    def problem6(self, a: List[int], b: List[int]) -> int:
        # Given two arrays of integers, compute the pair of values (one value
        # in each array) with the smallest (non-negative) difference. Return the
        # difference.
        
        # Complexity: O ( nm ) where n and m are the lengths of the 2 lists
        min_diff = float('inf')  # python specific MAX-INT
        for i in range(len(a)):
            for j in range(len(b)):
                diff = max(a[i], b[j]) - min(a[i], b[j])
                if diff == 0:
                    return 0
                min_diff = min(min_diff, diff)
        return min_diff
