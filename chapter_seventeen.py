from typing import List


class ChapterSeventeen:
    def _insert_min(self, min_arr: List[int], new_val: int) -> int:
        # min value is first, so pop can be used
        for i in range(len(min_arr)):
            prev_value = min_arr[i]
            if new_val < prev_value:
                min_arr.insert(i, new_val)
        
        min_arr.pop()  # remove final value
        return min_arr[-1]  # returns new threshold (max of the mins)
    
    def problem14(self, array: List[int], k: int) -> List[int]:
        # Design an algorithm to find the smallest K numbers in an array.
        
        # Complexity: O ( n * k ) at worst case, an array of descending values.
        max_int = 10000000  # Note: max int should be used here
        k_minimums = [max_int] * k
        threshold = max_int
        
        for i in range(len(array)):
            if array[i] < threshold:
                threshold = self._insert_min(k_minimums, array[i])
        return k_minimums
