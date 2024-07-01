from typing import List


class ChapterOne:
    def problem1(self, string: str) -> bool:
        # Implement an algorithm to determine if a string has all unique
        # characters. What if you cannot use additional data structures?
        
        # Complexity: basic hashmap approach is O( n ), Using an inplace sort
        # requires no additional space but will be O( n logn )
        string = ''.join(sorted([ch for ch in string]))
        
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return False
        return True

    def problem2(self, string_a: str, string_b: str) -> bool:
        # Given two strings,write a method to decide if one is a permutation of
        # the other.
        
        # Complexity: O( 2n + 2m ) where n is len(string_a) and m is
        # len(string_b).
        map_a = {}
        map_b = {}
        
        for ch in string_a:
            if ch in map_a:
                map_a[ch] += 1
            else:
                map_a[ch] = 1
                
        for ch in string_b:
            if ch in map_b:
                map_b[ch] += 1
            else:
                map_b[ch] = 1
                
        return map_a == map_b

    def problem3(self, char_arr: List[str]) -> List[str]:
        # Write a method to replace all spaces in a string with '%20'. You may
        # assume that the string has sufficient space at the end to hold the
        # additional characters,and that you are given the "true" length of the
        # string.
        
        # Complexity: amortized O( N ) since pythons append is O( 1 ) amortized
        # In place solution, using character array instead of string.
        url_arr = []
        for ch in char_arr:
            if ch == ' ':
                url_arr.append('%')
                url_arr.append('2')
                url_arr.append('0')
            else:
                url_arr.append(ch)
        return url_arr

    def problem4(self, string: str) -> bool:
        # Given a string, write a function to check if it is a permutation of
        # a palindrome. A palindrome is a word or phrase that is the same
        # forwards and backwards. A permutation is a rearrangement of letters.
        # The palindrome does not need to be limited to just dictionary words.

        # Complexity: O( 2n ) here, can be improved to O( n )
        char_count_parity = {}  # True if odd, False if even or 0
        for ch in string.lower():
            if ch not in char_count_parity:
                char_count_parity[ch] = True
            elif char_count_parity[ch]:
                char_count_parity[ch] = False
            elif not char_count_parity[ch]:
                char_count_parity[ch] = True

        # If there are more than 1 odd char repetition, it's not a palindrome.
        only_odds = len([b for b in char_count_parity.values() if b])
        return only_odds < 2

    def _check_for_replace(self, str_a: str, str_b: str, len_both: int) -> bool:
        outlier = None
        for i in range(len_both):
            if str_a[i] != str_b[i] and outlier is None:
                outlier = i
            elif str_a[i] != str_b[i]:  # outlier not none, more than one diff
                return False
        return True
    
    def _has_one_outlier_char(self, str_a: str, str_b: str) -> bool:
        charmap = {}
        for ch in str_a:
            if ch in charmap:
                charmap[ch] += 1
            else:
                charmap[ch] = 1
        
        for ch in str_b:
            if ch in charmap:
                charmap[ch] -= 1
            else:
                return False  # extra char has to be in larger one
        
        # can only be one
        outliers = [k for k, v in charmap.items() if v != 0]
        if len(outliers) > 1:
            return False
        return True
        
    def problem5(self, str_a: str, str_b: str) -> bool:
        # There are three types of edits that can be performed on strings:
        # insert a character, remove a character, or replace a character. Given
        # two strings, write a function to check if they are one edit (or zero
        # edits) away.
        
        # Complexity: at worst case O ( 2 (N+M) ) when inserted / removed char
        # at the end of the string
        len_a = len(str_a)
        len_b = len(str_b)
        
        if str_a == str_b:
            return True
        if max(len_a, len_b) - max(len_a, len_b) >= 2:
            return False
        if len_a == len_b:
            return self._check_for_replace(str_a, str_b, len_a)
        
        max_str, min_str = (str_a, str_b) if len_a > len_b else (str_b, str_a)
        return self._has_one_outlier_char(max_str, min_str)

    def problem6(self, string: str) -> str:
        # Implement a method to perform basic string compression using the
        # counts of repeated characters. For example, the string aabcccccaaa
        # would become a2b1c5a3. If the "compressed" string would not become
        # smaller than the original string, your method should return the
        # original string. You can assume the string has only uppercase and
        # lowercase letters (a - z).

        # Complexity: O(n)
        # Assuming case does matter, string is non-empty
        compressed_str = ''
        starting_char = string[0]
        char_count = 1
        string_len = len(string)
        for i in range(1, string_len):
            if string[i] == starting_char:
                char_count += 1
            else:
                compressed_str += starting_char + str(char_count)
                starting_char = string[i]
                char_count = 1

        # Last chars are not counted at end of loop
        compressed_str += starting_char + str(char_count)

        if len(compressed_str) < string_len:
            return compressed_str
        return string
    
    def problem7(self, _m: List[List[int]]) -> List[List[int]]:
        # Given an image represented by an NxN matrix, where each pixel in the
        # image is 4 bytes, write a method to rotate the image by 90 degrees.
        # Can you do this in place?
        
        # Complexity (in-place solution): O( n ^ 2 ) where n is the side length
        # of the matrix.
        
        # TRIVIAL CASES
        n = len(_m)
        if n == 1 or n == 0:
            return _m
        if n == 2:  # TODO swap is backwards
            _m[0][0], _m[0][1], _m[1][1], _m[1][0] = _m[0][1], _m[1][1], _m[1][0], _m[0][0]
            return _m
        
        # EACH LAYER HAS INIT POINT AND SWAPS ON THAT LAYER
        ini = {
            't': [0, 0],
            'r': [0, n - 1],
            'b': [n - 1, n - 1],
            'l': [n - 1, 0],
        }
        swap_offsets = [i for i in range(0, n-1)]
        while len(swap_offsets) > 1:
            
            # GET LIST OF SWAPS PER SIDE
            _sw = {  # sw for swaps
                't': [[ini['t'][0], x] for x in swap_offsets],
                'r': [[x, ini['r'][1]] for x in swap_offsets],
                'b': [[ini['b'][0], ini['b'][1] - x] for x in swap_offsets],
                'l': [[ini['l'][0] - x, ini['l'][1]] for x in swap_offsets],
            }
            
            # FOUR-WAY INPLACE SWAPS
            for i in range(len(swap_offsets)):
                t = _m[_sw['t'][i][0]][_sw['t'][i][1]]
                r = _m[_sw['r'][i][0]][_sw['r'][i][1]]
                b = _m[_sw['b'][i][0]][_sw['b'][i][1]]
                l = _m[_sw['l'][i][0]][_sw['l'][i][1]]
                
                # Over-optimizing here, could also use a single placeholder int
                _m[_sw['l'][i][0]][_sw['l'][i][1]], \
                    _m[_sw['b'][i][0]][_sw['b'][i][1]], \
                    _m[_sw['r'][i][0]][_sw['r'][i][1]], \
                    _m[_sw['t'][i][0]][_sw['t'][i][1]] = \
                    t, r, b, l
            
            # update inits:
            ini['t'][0] += 1
            ini['t'][1] += 1
            
            ini['r'][0] += 1
            ini['r'][1] -= 1
            
            ini['b'][0] -= 1
            ini['b'][1] -= 1
            
            ini['l'][0] -= 1
            ini['l'][1] += 1

            # get next layer swaps
            swap_offsets = swap_offsets[1:-1]
        return _m
    
    def problem8(self, matrix: List[List[int]]) -> List[List[int]]:
        # Write an algorithm such that if an element in an MxN matrix is 0,
        # its entire row and column are set to 0.
        
        # Complexity: O( 2MN ) for an MxN matrix
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])
        row_zeroes = set()
        col_zeroes = set()
        
        for row in range(row_cnt):
            for col in range(col_cnt):
                if matrix[row][col] == 0:
                    row_zeroes.add(row)
                    col_zeroes.add(col)
        
        for row in range(row_cnt):
            for col in range(col_cnt):
                if row in row_zeroes or col in col_zeroes:
                    matrix[row][col] = 0
        return matrix

    def problem9(self, s1: str, s2: str) -> bool:
        # Assume you have a method isSubstring which checks if one word is a
        # substring of another. Given two strings, sl and s2, write code to
        # check if s2 is a rotation of sl using only one call to isSubstring.
        
        # In python 'isSubstring' is done with the 'in' keyword
        # Complexity: O( 2n ) in theory, here O ( kn ) where k is constant
        return s2 in (s1 + s1)