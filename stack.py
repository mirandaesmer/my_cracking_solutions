from typing import Optional


class Stack:
    def __init__(self):
        self._stack_list = []
    
    def push(self, data: int) -> None:
        self._stack_list.append(data)
    
    def pop(self) -> int:
        if not self._stack_list:
            raise Exception("stack is empty")
        return self._stack_list.pop()

    def peek(self) -> Optional[int]:
        if self._stack_list:
            return self._stack_list[-1]
        return None
    
    def is_empty(self) -> bool:
        return bool(self._stack_list)
