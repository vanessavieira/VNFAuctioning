class Operator:
    num_services = 0

    def __init__(self, num_nodes, num_links, num_vnf_services, services_capacity):
        self.num_nodes = num_nodes
        self.num_links = num_links
        self.num_vnf_services = num_vnf_services
        self.services_capacity = services_capacity
        self.calculate_num_services()

    def calculate_num_services(self):
        self.num_services = self.num_links + self.num_vnf_services * self.num_nodes
