from typing import Set, List


class ChapterEight:
    def problem4(self, elements: Set[int]) -> List[Set[int]]:
        # Write a method to return all subsets of a set.
        
        # Trivial subsets
        len_elems = len(elements)
        subsets_by_level = {
            1: [{e} for e in elements],
            len_elems - 1: elements,
        }

        for subset_size in range(0, len_elems - 1):
            new_elements = []
            
            for s in subsets_by_level[subset_size + 1]:
                for e in elements:
                    if e not in s:  # avoid redundant add
                        
                        # only add non-duplicates
                        new_elem = s | {e}
                        if new_elem not in new_elements:
                            new_elements.append(new_elem)
            
            subsets_by_level[subset_size + 2] = new_elements.copy()
        
        # Unfold dictionary
        subsets = []
        for s_list in subsets_by_level.values():
            for s in s_list:
                subsets.append(s)
        return subsets

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
