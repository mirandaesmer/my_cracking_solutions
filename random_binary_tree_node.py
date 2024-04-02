from random import randint
from typing import List, Optional

from binary_tree_node import BinaryTreeNode


class RandomBinaryTree():
    def __init__(self):
        self._data_list: List[int] = []
        self.root = BinaryTreeNode()
        
    def insert(self, new_data: int) -> None:
        if new_data in self._data_list:
            raise Exception(f'Node with data {new_data} already exists')
        self._data_list.append(new_data)
        self.root.insert(new_data)
    
    def find(self, search_data: int) -> Optional[BinaryTreeNode]:
        if search_data not in self._data_list:
            return None
        return self.root.find(search_data)
    
    def delete(self, del_data: int) -> None:
        if del_data not in self._data_list:
            raise Exception('Node not in tree')
            
        # remove from data list
        idx = self._data_list.index(del_data)
        del self._data_list[idx]
        
        # remove actual node from tree,
        # TODO node is not removed from tree
        
    def get_random_node(self) -> BinaryTreeNode:
        if not self._data_list:
            raise Exception('No nodes in tree')
        rand_idx = randint(0, len(self._data_list) - 1)
        return self.root.find(self._data_list[rand_idx])
