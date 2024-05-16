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

    def _alt_subtraction(self, num_a: int, num_b: int) -> int:
        for _ in range(num_b):
            num_a += -1
        return num_a

    def _alt_multiplication(self, num_a: int, num_b: int) -> int:
        for _ in range(num_b):
            num_a += num_a
        return num_a
    
    def _alt_division(self, num_a: int, num_b: int) -> int:
        # Only integer (floor) division
        i = 0
        while i <= num_a:
            i += num_b
        return i
    
    def problem9(self, num_a: int, num_b: int, operation: str) -> Optional[int]:
        # Write methods to implement the multiply, subtract, and divide
        # operations for integers. The results of all of these are integers.
        # Use only the add operator.
        
        # Complexity: O ( m ) where m is the second operand for subtraction and
        # multiplication. For the division operation, the complexity depends on
        # the result: O( n / m )
        if operation == '-':
            return self._alt_subtraction(num_a, num_b)
        if operation == '*':
            return self._alt_multiplication(num_a, num_b)
        if operation == '/':
            return self._alt_division(num_a, num_b)
        return None

    def problem16(self, arr: List[int]) -> Tuple[int, int]:
        # Given an array of integers, write a method to find indices m and n
        # such that if you sorted elements m through n, the entire array would
        # be sorted. Minimize n - m (that is, find the smallest such sequence).
        
        # Complexity: Average case is O( k - (n + k - m) ) where k is the array
        # length, n and m are the indices as described. k - m is needed since a
        # reverse traversal is used. Worst case is a sorted array, O( k )
        n = 0
        m = arr_len = len(arr)
        
        for i in range(arr_len - 1):
            if arr[i] > arr[i + 1]:
                n = i + 1
                break
        
        for j in range(arr_len - 1, 1, -1):
            if arr[j] < arr[j - 1]:
                m = j
                break
        return n, m

    def _contains_operator(self, exp: str) -> bool:
        if '*' in exp or '/' in exp or '+' in exp or '-' in exp:
            return True
        return False
    
    def _apply_operator_by_index(self, expr: str, idx: int, op: str) -> str:
        # Performs operation in place
        next_idx = idx + 1
        prev_idx = idx - 1
        while prev_idx != 0 or expr[prev_idx] in ['*', '/', '+', '-']:
            prev_idx -= 1
        while next_idx != len(expr) - 1 or expr[next_idx] in ['*', '/', '+', '-']:
            next_idx += 1
        
        # tokenize
        prefix = expr[0: prev_idx]
        int_a = int(expr[prev_idx: idx])
        int_b = int(expr[idx: next_idx])
        suffix = expr[next_idx:]
        
        # apply operation and re-add to string
        result = ''
        if op == '*':
            result = str(int_a * int_b)
        elif op == '/':
            result = str(int_a / int_b)
        elif op == '+':
            result = str(int_a + int_b)
        elif op == '-':
            result = str(int_a - int_b)
        return prefix + result + suffix
    
    def problem26(self, expression: str) -> float:
        # Given an arithmetic equation consisting of positive integers:
        # +, -, * and / (no parentheses), compute the result.
        
        # TODO untested
        # Assuming everything is correctly formatted
        while self._contains_operator(expression):
            
            # order of operations, one operator per iteration
            if '*' in expression and '/' in expression:
                mul_idx = expression.index('*')
                div_idx = expression.index('/')
                if mul_idx < div_idx:
                    self._apply_operator_by_index(expression, mul_idx, '*')
                else:
                    self._apply_operator_by_index(expression, '/')
                
            elif '*' in expression:
                mul_idx = expression.index('*')
                self._apply_operator_by_index(expression, mul_idx, '*')
            elif '/' in expression:
                div_idx = expression.index('/')
                self._apply_operator_by_index(expression, div_idx, '/')
            
            elif '+' in expression and '-' in expression:
                add_idx = expression.index('+')
                sub_idx = expression.index('-')
                if add_idx < sub_idx:
                    self._apply_operator_by_index(expression, add_idx, '+')
                else:
                    self._apply_operator_by_index(expression, sub_idx, '-')

            elif '+' in expression:
                add_idx = expression.index('+')
                self._apply_operator_by_index(expression, add_idx, '+')
            elif '-' in expression:
                sub_idx = expression.index('-')
                self._apply_operator_by_index(expression, sub_idx, '-')

        return int(expression)
