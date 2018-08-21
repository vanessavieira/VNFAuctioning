from random import randint
import math
from Network.Dijkstra import shortest_path


class Bid:
    required_service_quantity = []
    total_required_service_quantity = 0
    valuation = 0
    sort_metric = 0
    input_node = 0
    output_node = 1
    shortest_node_path = []
    bandwidth_request = 0
    nodes_request = 0
    num_total_services_request = 0

    def __init__(self, client, operator, topology):
        self.client = client
        self.operator = operator
        self.topology = topology
        self.compute_bid_topology()
        self.compute_service_quantity()
        self.compute_valuation()
        self.compute_sort_metric()

    def compute_bid_topology(self):
        self.input_node = randint(0, len(self.topology.nodes) - 1)
        self.output_node = randint(0, len(self.topology.nodes) - 1)

        while self.output_node == self.input_node:
            self.output_node = randint(1, len(self.topology.nodes) - 1)

        for i in range(len(self.topology.nodes)):
            if i == self.input_node:
                self.input_node = self.topology.nodes[i]

            if i == self.output_node:
                self.output_node = self.topology.nodes[i]

        self.shortest_node_path = shortest_path(self.topology, "" + str(self.input_node) + "", "" + str(self.output_node) + "")

        print(self.shortest_node_path)
        print(len(self.shortest_node_path))

    def compute_service_quantity(self):
        self.required_service_quantity = []
        self.bandwidth_request = len(self.shortest_node_path) - 1
        self.nodes_request = len(self.shortest_node_path)

        num_vnf_services_request = self.nodes_request * self.operator.num_vnf_services
        if num_vnf_services_request > 7:
            num_vnf_services = randint(1, 7)
        else:
            num_vnf_services = randint(1, num_vnf_services_request)

        self.num_total_services_request = num_vnf_services + self.bandwidth_request

        for j in range(self.num_total_services_request):
            rand_quantity = randint(1, 30)
            self.total_required_service_quantity += rand_quantity
            self.required_service_quantity.append(rand_quantity)

        # print("input final " + str(input_node))
        # print("output final " + str(output_node))
        # print("Required service quantity: " + str(self.required_service_quantity))

    def compute_valuation(self):
        rand_valuation = randint(1, self.total_required_service_quantity)
        self.valuation = rand_valuation

        print("Valuation: " + str(self.valuation))

    def compute_sort_metric(self):
        self.sort_metric = self.valuation/(math.sqrt(self.total_required_service_quantity))
