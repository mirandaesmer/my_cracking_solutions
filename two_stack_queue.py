class TwoStackQueue:
    def __init__(self):
        self._data_stack = []
        self._pop_stack = []
    
    def push(self, new_data: int) -> None:
        self._data_stack.append(new_data)
        
    def pop(self) -> int:
        # Flip data into pop stack, simulating queue
        # O(2n) operation because data must be flipped back
        if not self._data_stack:
            raise Exception("stack is empty")
        
        stack_bottom = None
        while len(self._data_stack) > 1:
            self._pop_stack.append(self._data_stack.pop())
        stack_bottom = self._data_stack.pop()
        
        while self._pop_stack:
            self._data_stack.append(self._pop_stack.pop())
        return stack_bottom
