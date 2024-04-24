class ChapterOne:
    def problem1(self, string: str) -> bool:
        # Implement an algorithm to determine if a string has all unique
        # characters. What if you cannot use additional data structures?
        
        # Can be done with a hashmap, no additional DS constraint
        string = ''.join(sorted([ch for ch in string]))  # or in-place sort
        
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return False
        return True

    def problem2(self, string_a: str, string_b: str) -> bool:
        # Given two strings,write a method to decide if one is a permutation of
        # the other.
        
        # Complexity is O( 2n + 2m ) where n is len(string_a) and m is
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
