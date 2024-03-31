from linked_list_node import LinkedListNode


class AnimalShelterQueue:
    def __init__(self):
        self._arrival_incr = 0
        self.cat_root = LinkedListNode()
        self.dog_root = LinkedListNode()
    
    def enqueue(self, is_cat: bool) -> None:
        if is_cat:
            if self.cat_root is None:
                self.cat_root = LinkedListNode()
            self.cat_root.insert(self._arrival_incr)
        else:
            if self.dog_root is None:
                self.dog_root = LinkedListNode()
            self.dog_root.insert(self._arrival_incr)
        self._arrival_incr += 1
    
    def dequeue_cat(self) -> int:
        if self.cat_root.data is None:
            raise Exception("no more cats")
        
        deq_data = self.cat_root.data
        self.cat_root = self.cat_root.next
        return deq_data
    
    def dequeue_dog(self) -> int:
        if self.dog_root.data is None:
            raise Exception("no more cats")
        
        deq_data = self.dog_root.data
        self.dog_root = self.dog_root.next
        return deq_data
    
    def dequeue_any(self) -> int:
        if self.cat_root is None and self.dog_root is None:
            raise Exception("no animals")
        
        if self.cat_root is None:
            return self.dequeue_dog()
        elif self.dog_root is None:
            return self.dequeue_cat()
        
        if self.cat_root.data < self.dog_root.data:
            return self.dequeue_cat()
        return self.dequeue_dog()
