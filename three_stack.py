from stack import Stack


class ThreeStack(Stack):
    def __init__(self):
        super().__init__()
        self._array = [None] * 99  # can be increased dynamically
        self._first_stack_top = 0
        self._second_stack_top = 1
        self._third_stack_top = 2
        
    def push_on_stack(self, new_data: int, stack: int) -> None:
        if stack not in [1,2,3]:
            raise Exception("stack arg must be 1,2,3")
        
        if stack == 1:
            self._first_stack_top += 3
            self._array[self._first_stack_top] = new_data
        elif stack == 2:
            self._second_stack_top += 3
            self._array[self._second_stack_top] = new_data
        elif stack == 3:
            self._third_stack_top += 3
            self._array[self._third_stack_top] = new_data
    
    def pop_from_stack(self, stack: int) -> int:
        if stack not in [1, 2, 3]:
            raise Exception("stack arg must be 1,2,3")
        data = None
        
        if stack == 1:
            if self._first_stack_top == 0:
                raise Exception("stack is empty")
            data = self._array[self._first_stack_top]
            self._array[self._first_stack_top] = None
            self._first_stack_top -= 3
        elif stack == 2:
            if self._first_stack_top == 1:
                raise Exception("stack is empty")
            data = self._array[self._second_stack_top]
            self._array[self._second_stack_top] = None
            self._second_stack_top -= 3
        elif stack == 3:
            if self._first_stack_top == 2:
                raise Exception("stack is empty")
            data = self._array[self._third_stack_top]
            self._array[self._third_stack_top] = None
            self._third_stack_top -= 3
        return data
