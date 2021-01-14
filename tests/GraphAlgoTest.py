import math
from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class GraphAlgoTest(TestCase):

    def test_get_graph(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(ga.get_graph().get_all_v(), g.get_all_v())

    def test_save_and_load(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        ga.load_from_json("/data/A0.json")
        gg = ga.get_graph()
        self.assertIsNotNone(gg.get_all_v())
        ga.save_to_json("/data/save_test.json")
        ga.load_from_json("/data/A0.json")
        self.assertEqual(ga.get_graph().get_all_v(), gg.get_all_v())

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(12):
            g.add_node(i)
        g.add_edge(0, 6, 100)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 1)
        g.add_edge(5, 6, 1)
        ga = GraphAlgo(g)
        path = ga.shortest_path(0, 6)
        self.assertEqual(path, (6, list(range(7))))
        path = ga.shortest_path(0, 0)
        self.assertEqual(path, (0, [0]))
        path = ga.shortest_path(0, 200)
        self.assertEqual(path, (math.inf, []))

    def test_connected_component_in_graph_loaded(self):
        ga = GraphAlgo()
        ga.load_from_json("data/G_10_80_0.json")
        self.assertEqual(len(ga.connected_component(0)), ga.get_graph().v_size())

    def test_plot_graph(self):
        g = GraphAlgo()
        files = ["A0", "A1", "A2", "A3", "A4", "A5", "T0.json"]
        for i in range(len(files)):
            self.assertTrue(g.load_from_json("Data/"+files[i]))
            g.plot_graph()
