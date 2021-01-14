from unittest import TestCase
from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_add_node(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(node_id=i)
        self.assertEqual(g.v_size(), 12)

    def test_remove_node(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(node_id=i)
        g.add_edge(1, 2, 150)
        g.add_edge(1, 2, 150)
        g.add_edge(1, 3, 23)
        g.add_edge(3, 1, 195)
        g.add_edge(2, 1, 156)
        g.add_edge(20, 1, 156)
        self.assertEqual(g.e_size(), 4)
        self.assertEqual(g.v_size(), 12)
        g.remove_node(1)
        self.assertEqual(g.v_size(), 11)
        g.remove_node(1)

    def test_add_edge(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(node_id=i)
        g.add_edge(11, 5, 1)
        g.add_edge(9, 4, 1)
        g.add_edge(0, 18, 1)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 3, 1)
        g.add_edge(1, 15, 1)
        self.assertEqual(g.e_size(), 4)
        g.remove_edge(0, 0)
        g.remove_edge(11, 5)
        self.assertEqual(g.e_size(), 3)

    def test_get_all_v(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(node_id=i)
        self.assertEqual(len(g.get_all_v()), 12)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(node_id=i)
        g.add_edge(1, 2, 10)
        g.add_edge(1, 3, 10)
        g.add_edge(1, 4, 10)
        g.add_edge(1, 5, 10)
        g.add_edge(1, 6, 10)
        g.add_edge(1, 30, 10)
        self.assertEqual(len(g.all_out_edges_of_node(1)), 5)
        self.assertEqual(len(g.all_in_edges_of_node(1)), 0)

    def test_nodes(self):
        g = DiGraph()
        for i in range(1000 * 1000):
            g.add_node(i)
        for i in range(1000 * 100):
            g.add_edge(0, i, 1)
        g.add_edge(5, 6, 1)
        self.assertEqual(g.v_size(), 1000 * 1000)
        self.assertEqual(g.e_size(), 1000 * 100)
