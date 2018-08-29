from random import randint
import random
import itertools
import math
from Network.Dijkstra import shortest_path


class Bid:
    required_service_quantity = []
    total_required_vnf_service_quantity = 0
    valuation = 0
    sort_metric = 0
    input_node = 0
    output_node = 1
    shortest_node_path = []
    num_total_services_request = 0
    random_required_services = []
    services_to_choose = []

    def __init__(self, client, operator, topology):
        self.client = client
        self.operator = operator
        self.topology = topology
        self.compute_bid_topology()
        self.compute_vnf_service_request()
        self.compute_bandwidth_service_request()
        self.compute_valuation()
        self.compute_sort_metric()

    def compute_bid_topology(self):
        self.input_node = randint(0, len(self.topology.nodes) - 1)
        self.output_node = randint(0, len(self.topology.nodes) - 1)

        while self.output_node == self.input_node:
            self.output_node = randint(1, len(self.topology.nodes) - 1)

        for i in range(len(self.topology.nodes)):
            if i == self.input_node:
                self.input_node = self.topology.nodes[i].id

            if i == self.output_node:
                self.output_node = self.topology.nodes[i].id

        self.shortest_node_path = shortest_path(self.topology, str(self.input_node),
                                                str(self.output_node))

        print(self.shortest_node_path)
        print(len(self.shortest_node_path))

    def compute_vnf_service_request(self):
        num_services_requested = randint(1, 7)
        self.required_service_quantity = []

        for i in range(len(self.shortest_node_path)):
            self.services_to_choose.append(self.shortest_node_path[i].vnf_services)

        self.services_to_choose = list(itertools.chain(*self.services_to_choose))

        print("services_to_choose: " + str(self.services_to_choose))

        self.random_required_services = random.sample(self.services_to_choose, num_services_requested)
        print("random_services: " + str(self.random_required_services))

        for services in range(len(self.random_required_services)):
            rand_quantity = randint(1, 30)
            self.total_required_vnf_service_quantity += rand_quantity
            self.required_service_quantity.append(rand_quantity)

        print("Required service quantity: " + str(self.required_service_quantity))

    def compute_bandwidth_service_request(self):
        #TODO TERMINAR ISSO AQUI + AJEITAR IMPLEMENTAÇÃO FINAL!
        print("Required service quantity: " + str(self.required_service_quantity))

        path_nodes = []
        for i in range(len(self.shortest_node_path)):
            if (i+1) != len(self.shortest_node_path):
                edge_tuple = (self.shortest_node_path[i], self.shortest_node_path[i+1])
                path_nodes.append(edge_tuple)
        print("PATH NODES: " + str(path_nodes))

    def compute_valuation(self):
        rand_valuation = randint(1, self.total_required_vnf_service_quantity)
        self.valuation = rand_valuation

        print("Valuation: " + str(self.valuation))

    def compute_sort_metric(self):
        self.sort_metric = self.valuation/(math.sqrt(self.total_required_vnf_service_quantity))
