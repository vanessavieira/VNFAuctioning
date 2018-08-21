from VNFAuction.Bid import Bid
from VNFAuction.Operator import Operator
from VNFAuction import Auction
from Network.Graph import Graph
from Network.Dijkstra import shortest_path


def create_network_topology(topology):

    for node in ['A', 'B', 'C', 'D']:
        topology.add_node(node)

    topology.add_edge('A', 'B', 10)
    topology.add_edge('B', 'A', 10)
    topology.add_edge('A', 'C', 20)
    topology.add_edge('C', 'A', 20)
    topology.add_edge('B', 'D', 15)
    topology.add_edge('D', 'B', 15)
    topology.add_edge('C', 'D', 30)
    topology.add_edge('D', 'C', 30)

    # print(shortest_path(graph, 'A', 'C'))  # output: (25, ['A', 'B', 'D'])


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
    create_network_topology(topology)

    # Resource advertisement phase
    operator1 = Operator(num_nodes=4, num_links=4, num_vnf_services=5, service_capacity=100)

    # Bidding phase
    bidding(bids=bids, num_bids=num_bids, operator=operator1, topology=topology)

    # Winner determination & price computation phase
    auctioning(bids=bids, operator=operator1)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
