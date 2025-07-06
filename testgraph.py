# test_graph.py

import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        """Set up a fresh graph before each test."""
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 10)

    def test_add_vertex(self):
        """Test adding vertices to the graph."""
        self.graph.add_vertex("D")
        self.assertIn("D", self.graph.graph)

    def test_add_edge(self):
        """Test adding edges between vertices."""
        self.assertIn(("B", 5), self.graph.get_neighbors("A"))
        self.assertIn(("A", 5), self.graph.get_neighbors("B"))

    def test_is_path_bfs(self):
        """Test path existence using BFS/DFS."""
        self.assertTrue(self.graph.is_path("A", "C"))  # Path exists A → B → C
        self.assertFalse(self.graph.is_path("A", "D"))  # No path to D

    def test_display_graph(self):
        """Ensure the graph structure is correct."""
        self.graph.display_graph()

if __name__ == "__main__":
    unittest.main()
