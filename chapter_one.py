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
