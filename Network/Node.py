from Network.Service import Service


class Node:
    offered_services = []

    def __init__(self, id, num_vnf_services):
        self.id = id
        self.num_vnf_services = num_vnf_services
        self.compute_offered_services()

    def compute_offered_services(self):
        self.offered_services = []
        for i in range(self.num_vnf_services):
            service = Service(i, self.id)
            self.offered_services.append(service)
