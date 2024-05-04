from typing import Optional

from linked_list_node import LinkedListNode


class ChapterTwo:
    def problem1(self, root: LinkedListNode) -> Optional[LinkedListNode]:
        # Write code to remove duplicates from an unsorted linked list.
        
        # Complexity: O( n ), dedupe operation is a constant time operation.
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
        
        # Complexity: O( 2n ) at worst case
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
    
    def problem4(self, root: LinkedListNode, partition: int) -> LinkedListNode:
        # Write code to partition a linked list around a value x, such that all
        # nodes less than x come before all nodes greater than or equal to x. If
        # x is contained within the list, the values of x only need to be after
        # the elements less than x (see below). The partition element x can
        # appear anywhere in the "right partition"; it does not need to appear
        # between the left and right partitions.
        left_partition = LinkedListNode()
        right_partition = LinkedListNode()
        
        node = root
        while node is not None:
            if node.data < partition:
                left_partition.insert(node.data)
            else:
                right_partition.insert(node.data)
            node = node.next
        
        # Get last elem of left, can also be added to previous loop
        last_left = left_partition
        while last_left.next is not None:
            last_left = last_left.next
        last_left.next = right_partition
        
        return left_partition
    
    def problem5(
            self,
            root_a: LinkedListNode,
            root_b: LinkedListNode,
            reverse_order: bool = True
    ) -> LinkedListNode():
        # You have two numbers represented by a linked list, where each node
        # contains a single digit.The digits are stored in reverse order, such
        # that the 1 's digit is at the head of the list. Write a function
        # that adds the two numbers and returns the sum as a linked list.
        # Suppose the digits are stored in forward order. Repeat the above
        # problem.
        node_a = root_a
        node_b = root_b
        
        carry = 0
        sum_llist = LinkedListNode()
        if reverse_order:
            while not (node_a is None and node_b is None):
                local_sum = carry
                if node_a is not None:
                    local_sum += node_a.data
                    node_a = node_a.next
                if node_b is not None:
                    local_sum += node_b.data
                    node_b = node_b.next
                
                if local_sum < 10:
                    sum_llist.insert(local_sum)
                else:
                    carry = local_sum // 10
                    sum_llist.insert(local_sum % 10)
            
            if carry != 0:  # remaining carry:
                sum_llist.insert(carry)

        else:  # forward requires full traversal
            arr_a = []
            while node_a is not None:
                arr_a.append(str(node_a.data))
                node_a = node_a.next

            arr_b = []
            while node_b is not None:
                arr_b.append(str(node_b.data))
                node_b = node_b.next
            
            total_sum = int(''.join(arr_a)) + int(''.join(arr_b))
            total_sum_arr = [int(ch) for ch in str(total_sum)]
            for dig in total_sum_arr:
                sum_llist.insert(int(dig))
        return sum_llist
        
    def problem6(self, root: LinkedListNode) -> bool:
        # Implement a function to check if a linked list is a palindrome.
        
        # Complexity: O( 2n ), traversal and comparison are both O( n ).
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
        
        # Complexity: O( n ) best case, worst case is never more than O( n^2 )
        byref_map = {}
        node = root
        
        while True:
            if id(node) in byref_map:
                return byref_map[id(node)]
            else:
                byref_map[id(node)] = node
            node = node.next
            