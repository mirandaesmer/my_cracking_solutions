from typing import Set, List, Dict, Tuple, Optional

from image_array import ImageArray


class ChapterEight:
    def _memo_step_count(self, num: int, memo: Dict[int, int]) -> int:
        if num == 0:
            return 1
        if num <= 0:
            return 0
        if num in memo:
            return memo[num]
        
        ways = 0
        ways += self._memo_step_count(num - 3, memo)
        ways += self._memo_step_count(num - 2, memo)
        ways += self._memo_step_count(num - 1, memo)
        memo[num] = ways
        return ways
    
    def problem1(self, n: int) -> int:
        # A child is running up a staircase with n steps and can hop either 1
        # step, 2 steps, or 3 steps at a time. Implement a method to count how
        # many possible ways the child can run up the stairs.
        ways_map = {0: 1, 1: 1}  # trivial cases
        return self._memo_step_count(n, ways_map)
    
    def problem3(self, array: List[int]) -> Optional[int]:
        # A magic index in an array A[0... n-1] is defined to be an index such
        # that A[i] = i. Given a sorted array of distinct integers, write a
        # method to find a magic index, if one exists, in array A.
        
        # Complexity: O( n ) at worst. Since array is made up of distinct
        # sorted integers, we can return whenever the value is greater than the
        # index.
        for i in range(len(array)):
            if array[i] > i:
                return None
            if array[i] == i:
                return i
        return None

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
    
    def _rec_perms(
            self,
            curr_chars: List[str],
            rem_chars: List[str],
            all_perms: List[str] = [],
    ) -> None:
        if len(rem_chars) == 0:
            all_perms.append(''.join(curr_chars))
            return
        
        for i in range(len(rem_chars)):
            curr_copy = curr_chars.copy()
            curr_copy.append(rem_chars[i])
            rem_copy = rem_chars.copy()
            del rem_copy[i]
            
            self._rec_perms(curr_copy, rem_copy, all_perms)
    
    def problem8(self, string: str) -> List[str]:
        # Write a method to compute all permutations of a string of unique
        # characters.
        
        # Complexity is O ( n! ) where n is the len of string.
        # TODO still untested
        perms = []
        char_arr = [ch for ch in string]
        self._rec_perms([], char_arr, perms)
        return perms
    
    def problem10(
            self,
            arr: List[List[int]],
            point: Tuple[int, int],
            new_color: int,
    ) -> List[List[int]]:
        # Implement the "paint fill" function that one might see on many image
        # editing programs. That is, given a screen (represented by a
        # two-dimensional array of colors), a point, and a new color, fill in
        # the surrounding area until the color changes from the original color.
        
        # Complexity: O ( 9 * n * m ) where n and m are the dimensions of the
        # image array. This is because in the worst case every pixel will be
        # painted. See class ImageArray in image_array.py.
        im = ImageArray(arr)
        selection_color: int = arr[point[0]][point[1]]
        next_points: Set[Tuple[int, int]] = {point}
        
        while next_points:
            curr_points: Set[Tuple[int, int]] = next_points.copy()
            next_points: Set[Tuple[int, int]] = set([])
            
            for curr_pt in curr_points:
                top = im.get_top(curr_pt)
                bottom = im.get_bottom(curr_pt)
                left = im.get_left(curr_pt)
                right = im.get_right(curr_pt)
                
                # NOTE: constant time, 4 directions
                for pt in [top, bottom, left, right]:
                    if im.get_point(pt) == selection_color:
                        next_points.add(pt)
                
                # change color of visited point
                arr[curr_pt[0]][curr_pt[1]] = new_color
        
        return im.image_array
