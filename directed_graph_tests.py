from unittest import TestCase

from directed_graph import DirectedGraph, GraphNode


class DirectedGraphTests(TestCase):
    def setUp(self):
        self.dg = DirectedGraph()
        
        self.nodes = [GraphNode(i, set()) for i in range(0, 10)]
        for n in self.nodes:
            self.dg.add_node(n)
        self.dg.add_connection(self.nodes[1], self.nodes[2])
        self.dg.add_connection(self.nodes[1], self.nodes[3])
        self.dg.add_connection(self.nodes[2], self.nodes[4])
        self.dg.add_connection(self.nodes[2], self.nodes[5])
        self.dg.add_connection(self.nodes[3], self.nodes[6])
        self.dg.add_connection(self.nodes[4], self.nodes[7])
        self.dg.add_connection(self.nodes[4], self.nodes[2])
        self.dg.add_connection(self.nodes[6], self.nodes[8])
        self.dg.add_connection(self.nodes[8], self.nodes[3])
        self.dg.add_connection(self.nodes[0], self.nodes[7])
    
    def test_add_node(self) -> None:
        dg = DirectedGraph()
        self.assertEqual(dg._node_data, set())
        
        nodes = [GraphNode(i, set()) for i in range(0, 10)]
        for n in nodes:
            dg.add_node(n)
        self.assertEqual(sorted(dg._node_data), list(range(0, 10)))
        
        with self.assertRaises(Exception):
            dg.add_node(GraphNode(2, set()))
    
    def test_add_connection(self) -> None:
        # see test setup
        exp_adjacency_map = {
            0: {7},  # nothing points to 0
            1: {2, 3},
            2: {4, 5},
            3: {6},
            4: {2, 7},  # (2-4 is a loop)
            5: set(),
            6: {8},
            7: set(),
            8: {3},  # (3-6-8 is a loop)
            9: set(),  # isolated node
        }
        self.assertEqual(self.dg._adjacency_map, exp_adjacency_map)
    
    def test_bfs(self) -> None:
        # base cases
        self.assertEqual(self.dg.bfs(self.nodes[1], 1), self.nodes[1])
        self.assertIsNone(self.dg.bfs(self.nodes[1], 11))
        
        # no valid route
        self.assertIsNone(self.dg.bfs(self.nodes[9], 1))
        self.assertIsNone(self.dg.bfs(self.nodes[6], 1))
        self.assertIsNone(self.dg.bfs(self.nodes[0], 6))
        
        # valid routes, different path sizes
        self.assertEqual(self.dg.bfs(self.nodes[1], 2), self.nodes[2])
        self.assertEqual(self.dg.bfs(self.nodes[1], 5), self.nodes[5])
        self.assertEqual(self.dg.bfs(self.nodes[1], 8), self.nodes[8])
