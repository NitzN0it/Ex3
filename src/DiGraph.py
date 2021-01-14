from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes: {int, Node} = dict()
        self.neighIn: {int, {int, float}} = dict()
        self.neighOut: {int, {int, float}} = dict()
        self.MC = 0
        self.edge_size = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edge_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.neighIn[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.neighOut[id1]

    def get_mc(self) -> int:
        return self.MC

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(k=node_id, loc=pos)
        self.neighIn[node_id] = {}
        self.neighOut[node_id] = {}
        self.MC += 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight <= 0:
            return False
        if id1 == id2:
            return False
        if id1 not in self.nodes or id2 not in self.nodes:
            return False
        if id2 in self.neighOut.get(id1):
            return False
        self.neighOut[id1][id2] = weight
        self.neighIn[id2][id1] = weight
        self.MC += 1
        self.edge_size += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        self.edge_size -= len(self.neighIn[node_id]) + len(self.neighOut[node_id])
        self.neighIn.pop(node_id)
        self.neighOut.pop(node_id)
        self.nodes.pop(node_id)
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        if node_id1 not in self.neighIn[node_id2] or node_id2 not in self.neighOut[node_id1]:
            return False
        self.edge_size -= 1
        self.neighOut[node_id1].pop(node_id2)
        self.neighIn[node_id2].pop(node_id1)
        self.MC += 1
        return True

    def get_node(self, node):
        return self.nodes[node]
