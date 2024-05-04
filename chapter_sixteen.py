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
