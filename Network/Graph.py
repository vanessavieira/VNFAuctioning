from collections import defaultdict


class Graph(object):
    nodes = []

    def __init__(self):
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
