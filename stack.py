class Stack:
    def __init__(self):
        self._stack_list = []
    
    def push(self, data: int) -> None:
        self._stack_list.append(data)
    
    def pop(self) -> int:
        if not self._stack_list:
            raise Exception("stack is empty")
        return self._stack_list.pop()
