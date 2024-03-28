class ThreeStack:
    def __init__(self):
        super().__init__()
        self._array = [None] * 99  # can be increased dynamically
        self._stack_top_map = {
            1: None,
            2: None,
            3: None,
        }
        
    def push_on_stack(self, new_data: int, stack: int) -> None:
        if stack not in [1, 2, 3]:
            raise Exception("stack arg must be 1,2,3")
        
        if self._stack_top_map[stack] is None:
            arr_idx = stack - 1
            self._stack_top_map[stack] = arr_idx
            self._array[arr_idx] = new_data
        else:
            self._stack_top_map[stack] += 3
            self._array[self._stack_top_map[stack]] = new_data
    
    def pop_from_stack(self, stack: int) -> int:
        if stack not in [1, 2, 3]:
            raise Exception("stack arg must be 1,2,3")
        
        pop_data = None
        if self._stack_top_map[stack] is None:
            raise Exception("stack is empty")
        if self._stack_top_map[stack] == stack - 1:
            pop_data = self._array[self._stack_top_map[stack]]
            self._stack_top_map[stack] = None
        else:
            pop_data = self._array[self._stack_top_map[stack]]
            self._stack_top_map[stack] -= 3
        
        return pop_data
