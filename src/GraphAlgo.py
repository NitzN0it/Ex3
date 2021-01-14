import json
import math
import random

import matplotlib.pyplot as plt
from typing import List
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.Node import Node


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        try:
            with open(file_name, "r") as file:
                json_file = json.load(file)
                positions = []
                for node in json_file['Nodes']:
                    if "pos" in node:
                        for pos in node['pos'].split(','):
                            positions.append(float(pos))
                    else:
                        positions = [0, 0, 0]
                    g.add_node(node['id'], (positions[0], positions[1], positions[2]))
                    positions.clear()
                for edge in json_file['Edges']:
                    g.add_edge(edge['src'], edge['dest'], edge['w'])
            self.graph = g
            return True
        except IOError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                file.write(str(self.graph))
                return True
        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return math.inf, []
        if id1 == id2:
            return 0, [id1]
        self.dijkstra_algo(id1)
        dist = self.graph.get_all_v().get(id2).getWeight()
        if dist == math.inf:
            return math.inf, []
        path = []
        path.insert(0, id2)
        parent = self.graph.get_all_v().get(id2)
        while parent.getInfo() != 0:
            path.insert(0, parent.getInfo())
            parent = self.graph.get_all_v().get(parent.getInfo())
        path.insert(0, id1)
        return dist, path

    def connected_component(self, id1: int) -> list:
        if not self.graph.get_all_v():
            return []
        self.reset_tag()
        t = Tarjan(self.graph)
        return t.start(id1)

    def connected_components(self) -> List[list]:
        if not self.graph.get_all_v():
            return [[]]
        self.reset_tag()
        t = Tarjan(self.graph)
        return t.start(-1)

    def plot_graph(self) -> None:
        graph = self.get_graph()
        for id in graph.get_all_v().keys():
            for k, w in graph.all_out_edges_of_node(id).items():
                x1: int = graph.get_all_v().get(id).getLocation()[0]
                y1: int = graph.get_all_v().get(id).getLocation()[1]
                x2: int = graph.get_all_v().get(k).getLocation()[0]
                y2: int = graph.get_all_v().get(k).getLocation()[1]
                plt.arrow(x1, y1, (x2 - x1), (y2 - y1), length_includes_head=True, width=0.00002, head_width=0.0002)
        for node in graph.get_all_v().values():
            node: Node = node
            if node.getLocation() is None or node.getLocation() == (0, 0, 0):
                node.setLocation((random.uniform(35.18, 35.2), random.uniform(32.1, 32.2), 0))
            plt.plot(node.getLocation()[0], node.getLocation()[1], 'or', markersize=10)
            plt.text(node.getLocation()[0], node.getLocation()[1], str(node.getKey()))
        plt.show()

    def dijkstra_algo(self, src_id):
        self.inf_weight()
        q = PriorityQueue()
        src_node = self.graph.get_all_v().get(src_id)
        src_node.setWeight(0)
        q.add(src_node)
        while not q.isEmpty():
            current = q.pop()
            for node, weight in self.graph.all_out_edges_of_node(current.getKey()).items():
                next_node = self.graph.get_all_v().get(node)
                if next_node.getWeight() > current.getWeight() + weight:
                    next_node.setWeight(current.getWeight() + weight)
                    q.add(next_node)
                    next_node.setInfo(current.getKey())

    def inf_weight(self):
        for node in self.graph.get_all_v().values():
            node.setWeight(math.inf)

    def reset_tag(self):
        for node in self.graph.get_all_v().values():
            node.setTag(-1)
            node.setInfo(-1)


class Tarjan:

    def __init__(self, g: DiGraph):
        self.graph = g
        self.list_of_paths = []
        self.stack = []
        self.onStack = {}
        self.id = 0

    def start(self, src_id=-1) -> List[list]:
        self.onStack = dict()
        path = []
        if src_id != -1:
            self.dfs(src_id)
            for i in self.graph.get_all_v().values():
                if self.graph.get_all_v().get(src_id).getInfo() == i.getInfo():
                    path.append(i.getKey())
            return path
        self.update_onStack()
        for i in self.graph.get_all_v().values():
            if i.getTag() == -1:
                self.dfs(i.getKey())
        for count in range(len(self.graph.get_all_v()) + 1):
            for i in self.graph.get_all_v().values():
                if count == i.getInfo():
                    path.append(i.getKey())
            if path:
                self.list_of_paths.append(path[:])
            path.clear()
        return self.list_of_paths

    def update_onStack(self):
        for node in self.graph.get_all_v().keys():
            self.onStack.update({node: False})

    def dfs(self, at):
        at_node = self.graph.get_all_v().get(at)
        self.stack.append(at_node)
        self.id += 1
        at_node.setTag(self.id)
        at_node.setInfo(self.id)
        self.onStack.update({at: True})

        for to in self.graph.all_out_edges_of_node(at):
            to_node = self.graph.get_all_v().get(to)
            if to_node.getTag() == -1:  # unvisited
                self.dfs(to)
            if self.onStack.get(to):
                at_node.setInfo(min(at_node.getInfo(), to_node.getInfo()))

        if at_node.getTag() == at_node.getInfo():
            while self.stack:
                node = self.stack.pop()
                self.onStack.update({node.getKey(): False})
                node.setInfo(at_node.getInfo())
                if node.getKey() == at_node.getKey():
                    break


class PriorityQueue(Node):

    def __init__(self):
        self.q = []

    def add(self, node):
        self.q.append(node)

    def isEmpty(self):
        return len(self.q) == 0

    def find_min(self) -> Node:
        min = 0
        for i in range(len(self.q)):
            if self.q[i].getWeight() < self.q[min].getWeight():
                min = i
        return self.q[min]

    def peek(self) -> Node:
        return self.find_min()

    def pop(self):
        node = self.find_min()
        self.q.remove(node)
        return node
