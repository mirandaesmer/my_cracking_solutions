from stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self._min = None
    
    def push(self, data: int) -> None:
        super().push(data)
        self._min = min(self._min, data)
    
    def pop(self) -> int:
        # Amortized O(1)
        popped_data = super().pop()
        if not self._stack_list:  # no more data
            self._min = None
        elif popped_data == self._min:
            self._min = min(self._stack_list)
        return popped_data
    
    def min(self) -> int:
        return self._min
