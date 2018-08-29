from collections import defaultdict
from Network.Service import Service


class Graph(object):

    def __init__(self):
        self.edge_list = defaultdict(list)
        self.edges = []
        self.distances = {}
        self.nodes = []
        self.bandwidth_service = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edge_list[edge.from_node].append(edge.to_node)
        # self.edge_list[to_node].append(from_node)
        self.distances[(edge.from_node, edge.to_node)] = edge.distance
        self.edges.append(edge)

        service = Service(id=edge, node="no node", type="bandwidth")
        self.bandwidth_service.append(service)
        # print("bandwidth service: " + str(self.bandwidth_service))
