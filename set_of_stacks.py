class SetOfStacks:
    def __init__(self, threshold: int):
        self._stack_arr = []
        self._threshold = threshold
    
    def push(self, new_data: int) -> None:
        if self._stack_arr:  # data already exists
            if len(self._stack_arr[-1]) < self._threshold:
                self._stack_arr[-1].append(new_data)
            else:
                self._stack_arr.append([new_data])
        else:  # no data yet
            self._stack_arr.append([new_data])
    
    def pop(self) -> int:
        if not self._stack_arr:  # no data yet
            raise Exception("SetOfStacks is empty")
    
        if len(self._stack_arr[-1]) == 1:
            pop_data = self._stack_arr[-1][0]
            del self._stack_arr[-1]
        else:
            pop_data = self._stack_arr[-1][-1]
            del self._stack_arr[-1][-1]
        
        return pop_data
    
    def pop_at(self, index: int) -> int:
        if not self._stack_arr or len(self._stack_arr) <= index:
            raise Exception("index of of range")
        
        if len(self._stack_arr[index]) == 1:
            pop_data = self._stack_arr[index][0]
            del self._stack_arr[index]
        else:
            pop_data = self._stack_arr[index][-1]
            del self._stack_arr[index][-1]
        return pop_data