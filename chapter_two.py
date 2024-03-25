from typing import Optional

from linked_list_node import LinkedListNode


class ChapterTwo:
    def problem1(self, root: LinkedListNode) -> Optional[LinkedListNode]:
        # Write code to remove duplicates from an unsorted linked list.
        if root is None or root.data is None:
            return None
        
        duplicates_map = {root.data: True}
        node = root
        while node.next is not None:
            
            # Remove duplicate if found
            if node.next.data in duplicates_map:
                node.next = node.next.next
            else:
                duplicates_map[node.next.data] = True
            
            node = node.next
        return root
    
    def problem2(
            self,
            root: LinkedListNode,
            k: int
    ) -> Optional[LinkedListNode]:
        # Implement an algorithm to find the kth to last element of a singly
        # linked list.
        if root is None or root.data is None:
            return None
        
        kth_back = root
        node = root
        for _ in range(0, k):
            if node.next is None:  # Less than k nodes
                return None
            node = node.next
        
        while True:
            if node.next is None:
                return kth_back
            node = node.next
            kth_back = kth_back.next
    
    def problem6(self, root: LinkedListNode) -> bool:
        # Implement a function to check if a linked list is a palindrome.
        if root is None or root.data is None:
            return False
        
        node = root
        data_list = [root.data]
        while node.next is not None:
            data_list.append(node.next.data)
            node = node.next
        
        return data_list == data_list[::-1]

    def problem7(self, root_a: LinkedListNode, root_b: LinkedListNode) -> bool:
        # Given two (singly) linked lists, determine if the two lists intersect.
        # Return the intersecting node. Note that the intersection is defined
        # based on reference, not value.That is, if the kth node of the first
        # linked list is the exact same node (by reference) as the jth node of
        # the second linked list, then they are intersecting.
        byref_map = {}
        node_a = root_a
        node_b = root_b
        
        while node_a is not None:
            byref_map[id(node_a)] = node_a
            node_a = node_a.next
        
        while node_b is not None:
            if id(node_b) in byref_map:
                return True
            node_b = node_b.next
            
        return False

    def problem8(self, root: LinkedListNode) -> LinkedListNode:
        # Given a circular linked list, implement an algorithm that returns the
        # node at the beginning of the loop.
        byref_map = {}
        node = root
        
        while True:
            if id(node) in byref_map:
                return byref_map[id(node)]
            else:
                byref_map[id(node)] = node
            node = node.next
            