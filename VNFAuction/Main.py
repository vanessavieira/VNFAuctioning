from VNFAuction.Bid import Bid
from VNFAuction.Operator import Operator
from VNFAuction import Auction
from Network.Graph import Graph
from Network.Node import Node
from Network.Dijkstra import shortest_path


def create_network_topology(topology, num_vnf_services):

    node1 = Node(id="A", num_vnf_services=num_vnf_services)
    node2 = Node(id="B", num_vnf_services=num_vnf_services)
    node3 = Node(id="C", num_vnf_services=num_vnf_services)
    node4 = Node(id="D", num_vnf_services=num_vnf_services)

    topology.add_node(node1)
    topology.add_node(node2)
    topology.add_node(node3)
    topology.add_node(node4)

    topology.add_edge(node1.id, node2.id, 10)
    topology.add_edge(node2.id, node1.id, 10)
    topology.add_edge(node1.id, node3.id, 20)
    topology.add_edge(node3.id, node1.id, 20)
    topology.add_edge(node2.id, node4.id, 15)
    topology.add_edge(node4.id, node2.id, 15)
    topology.add_edge(node3.id, node4.id, 30)
    topology.add_edge(node4.id, node3.id, 30)

    # print(shortest_path(topology, node1.id, node4.id))


def bidding(bids, num_bids, operator, topology):
    for i in range(num_bids):
        bids.append(Bid("client" + str(i), operator, topology))


def auctioning(bids, operator):
    Auction.Auction(bids, operator)
    bids.clear()


def main():

    num_bids = 100
    bids = []
    topology = Graph()

    # Create network topology
    create_network_topology(topology, num_vnf_services=5)

    # Resource advertisement phase
    operator1 = Operator(num_nodes=4, num_links=4, num_vnf_services=5, service_capacity=100)

    # Bidding phase
    bidding(bids=bids, num_bids=num_bids, operator=operator1, topology=topology)

    # Winner determination & price computation phase
    auctioning(bids=bids, operator=operator1)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
