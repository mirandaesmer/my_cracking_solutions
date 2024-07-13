from typing import List

from linked_list_node import LinkedListNode


class ExtraProblems:
    def problem1(self, root_nodes: List[LinkedListNode]) -> LinkedListNode:
        # You are given an array of k linked-lists lists, each linked-list is
        # sorted in ascending order. Merge all the linked-lists into one sorted
        # linked-list and return it.
        
        # Complexity: O ( n ^ 2 ) at worst where n is the total amount of nodes.
        sorted_root = LinkedListNode()
        valid_nodes = [n for n in root_nodes if n is not None]
        
        while len(valid_nodes) != 0:
            # add min_value to new LL
            nodes_data = [n.data for n in valid_nodes]
            min_value = min(nodes_data)  #
            sorted_root.insert(min_value)
            
            # advance the minimum node only
            idx = nodes_data.index(min_value)
            valid_nodes[idx] = valid_nodes[idx].next
            
            valid_nodes = [n for n in valid_nodes if n is not None]
        return sorted_root
