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
