from VNFAuction.Bid import Bid
from VNFAuction.Operator import Operator
from VNFAuction import Auction
from Network.Graph import Graph
from Network.Node import Node
from Network.Edge import Edge
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

    edge1 = Edge(from_node=node1.id, to_node=node2.id, distance=10)
    edge2 = Edge(from_node=node2.id, to_node=node1.id, distance=10)
    edge3 = Edge(from_node=node1.id, to_node=node3.id, distance=20)
    edge4 = Edge(from_node=node3.id, to_node=node1.id, distance=20)
    edge5 = Edge(from_node=node2.id, to_node=node4.id, distance=15)
    edge6 = Edge(from_node=node4.id, to_node=node2.id, distance=15)
    edge7 = Edge(from_node=node3.id, to_node=node4.id, distance=30)
    edge8 = Edge(from_node=node4.id, to_node=node3.id, distance=30)

    topology.add_edge(edge1)
    topology.add_edge(edge2)
    topology.add_edge(edge3)
    topology.add_edge(edge4)
    topology.add_edge(edge5)
    topology.add_edge(edge6)
    topology.add_edge(edge7)
    topology.add_edge(edge8)

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
    operator1 = Operator(num_nodes=4, num_links=4, num_vnf_services=5, service_capacity=100, topology=topology)

    # Bidding phase
    bidding(bids=bids, num_bids=num_bids, operator=operator1, topology=topology)

    # Winner determination & price computation phase
    auctioning(bids=bids, operator=operator1)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
