class ChapterEight:
    
    def _rec_multiply(self, num: int, steps: int, total: int) -> int:
        if steps == 0:
            return total
        return self._rec_multiply(num, steps - 1, total + num)
    
    def problem5(self, num_a: int, num_b: int) -> int:
        # Write a recursive function to multiply two positive integers without
        # using the *operator.You can use addition, subtraction, and bit
        # shifting, but you should minimize the number of those operations.
        
        # Complexity: O( m ) where 'n, m' are the 2 numbers to be added.
        # Consider the case where n is 99 and m is 1, there will only be 1
        # function call.
        if num_a == 0 or num_b == 0:
            return 0
        return self._rec_multiply(num_a, num_b, 0)
