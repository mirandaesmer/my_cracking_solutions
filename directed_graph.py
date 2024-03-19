from __future__ import annotations

from typing import Dict, Set, Optional, List


class GraphNode:
    def __init__(self, data: int, children: Set[GraphNode]) -> None:
        self.data = data
        self.children = children


class DirectedGraph:
    def __init__(self):
        self._adjacency_map: Dict[int, Set[int]] = {}
        self._nodes = []
        self._node_data = set()  # to avoid repeats
        
    def add_node(self, new_node: GraphNode) -> None:
        if new_node.data in self._node_data:
            raise Exception('node already exists')
        self._node_data.add(new_node.data)
        self._nodes.append(new_node)
        self._adjacency_map[new_node.data] = set()
    
    def add_connection(self, from_node: GraphNode, to_node: GraphNode):
        if from_node.data not in self._node_data:
            raise Exception('node does not exist in graph')
        if to_node.data not in self._node_data:
            raise Exception('Node does not exist in graph')
        if to_node in from_node.children:
            raise Exception('Nodes already connected')
        
        from_node.children.add(to_node)
        (self._adjacency_map[from_node.data]).add(to_node.data)
    
    def bfs(self, root: GraphNode, target_data: int) -> Optional[GraphNode]:
        if root.data == target_data:
            return root
        if target_data not in self._node_data:
            return None
        if root.data not in self._node_data:
            return None
        
        nodes_already_searched = [root]
        nodes_to_search = list(root.children)
        no_more_nodes = bool(nodes_already_searched)
        
        while no_more_nodes:
            next_level = []
            for nd in nodes_to_search:
                if nd.data == target_data:
                    return nd
                nodes_already_searched.append(nd)
                
                for ch in nd.children:
                    if ch not in next_level and ch not in nodes_already_searched:  # dupes
                        next_level.append(ch)
                        
            nodes_to_search = next_level
            no_more_nodes = bool(next_level)
        return None

    def dfs(
            self,
            node: GraphNode,
            target: GraphNode,
            path: List[GraphNode],
            visited: Set[GraphNode],
    ) -> List[GraphNode]:
        # Greedy, returns first valid path, or None
        if node == target:
            return path + [target]

        visited.add(node)
        search_space = node.children - visited
        
        for adj in search_space:
            pos_path = self.dfs(adj, target, path + [node], visited)
            if pos_path is not None:
                return pos_path
