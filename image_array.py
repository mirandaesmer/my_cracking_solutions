from typing import List, Tuple, Optional


class ImageArray:
    def __init__(self, arr: List[List[int]]) -> None:
        self.image_array = arr
        self._row_len = len(arr[0])
        self._col_len = len(arr)
    
    def get_point(self, pt: Tuple[int, int]) -> Optional[int]:
        try:
            val = self.image_array[pt[0]][pt[1]]
            return val
        except Exception:
            return None
    
    def get_top(self, pt: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if pt[0] != 0:
            return pt[0] - 1, pt[1]
        return None
    
    def get_bottom(self, pt: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if pt[0] != self._col_len - 1:
            return pt[0] + 1, pt[1]
        return None
    
    def get_left(self, pt: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if pt[1] != 0:
            return pt[0], pt[1] - 1
        return None
    
    def get_right(self, pt: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if pt[1] != self._row_len - 1:
            return pt[0], pt[1] + 1
        return None
