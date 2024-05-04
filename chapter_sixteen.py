from typing import Tuple


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
