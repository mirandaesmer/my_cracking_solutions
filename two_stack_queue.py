class TwoStackQueue:
    def __init__(self):
        self._stack_one = []
        self._stack_two = []
        self._use_first = bool
    
    def push(self, new_data: int) -> None:
        if self._use_first:
            self._stack_one.append(new_data)
        else:
            self._stack_two.append(new_data)
        
    def pop(self) -> int:
        if self._use_first and not self._stack_one:
            raise Exception("stack is empty")
        if not self._use_first and not self._stack_two:
            raise Exception("stack is empty")
        
        # Flip stack onto another, simulating queue, O(n) operation
        stack_bottom = None
        if self._use_first:
            while len(self._stack_one) > 1:
                self._stack_two.append(self._stack_one.pop())
            stack_bottom = self._stack_one.pop()
        else:
            while len(self._stack_two) > 1:
                self._stack_one.append(self._stack_two.pop())
            stack_bottom = self._stack_one.pop()
        
        self._use_first = not self._use_first
        return stack_bottom
