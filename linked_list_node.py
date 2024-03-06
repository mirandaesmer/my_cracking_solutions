from __future__ import annotations
from typing import Optional


class LinkedListNode:
    def __init__(
            self,
            data: int = None,
            _next: Optional[LinkedListNode] = None):
        self.data = data
        self.next = _next
    
    def insert(self, new_data: int) -> None:
        if self.data is None:
            self.data = new_data
        elif self.next is None:
            self.next = LinkedListNode(data=new_data)
        else:
            return self.next.insert(new_data)
