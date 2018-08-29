import itertools


class Operator:
    num_services = 0
    services = []

    def __init__(self, num_nodes, num_links, num_vnf_services, service_capacity, topology):
        self.num_nodes = num_nodes
        self.num_links = num_links
        self.topology = topology
        self.num_vnf_services = num_vnf_services
        self.service_capacity = service_capacity
        self.calculate_num_services()
        self.calculate_services()

    def calculate_num_services(self):
        self.num_services = self.num_links + self.num_vnf_services * self.num_nodes

    def calculate_services(self):

        for i in range(len(self.topology.nodes)):
            self.services.append(self.topology.nodes[i].vnf_services)

        self.services = list(itertools.chain(*self.services))
        # print("services: " + str(self.services))
