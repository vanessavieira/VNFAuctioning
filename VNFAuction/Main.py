from VNFAuction.Bid import Bid
from VNFAuction.Operator import Operator
from VNFAuction import Auction
from Network.Graph import Graph
from Network.Node import Node
from Network.Edge import Edge


def create_network_topology(topology, num_vnf_services):

    nodeA = Node(id="A", num_vnf_services=num_vnf_services)
    nodeB = Node(id="B", num_vnf_services=num_vnf_services)
    nodeC = Node(id="C", num_vnf_services=num_vnf_services)
    nodeD = Node(id="D", num_vnf_services=num_vnf_services)
    nodeE = Node(id="E", num_vnf_services=num_vnf_services)
    nodeF = Node(id="F", num_vnf_services=num_vnf_services)
    nodeG = Node(id="G", num_vnf_services=num_vnf_services)
    nodeH = Node(id="H", num_vnf_services=num_vnf_services)
    nodeI = Node(id="I", num_vnf_services=num_vnf_services)
    nodeJ = Node(id="J", num_vnf_services=num_vnf_services)

    topology.add_node(nodeA)
    topology.add_node(nodeB)
    topology.add_node(nodeC)
    topology.add_node(nodeD)
    topology.add_node(nodeE)
    topology.add_node(nodeF)
    topology.add_node(nodeG)
    topology.add_node(nodeH)
    topology.add_node(nodeI)
    topology.add_node(nodeJ)

    edgeAB = Edge(from_node=nodeA, to_node=nodeB, distance=10)
    edgeBA = Edge(from_node=nodeB, to_node=nodeA, distance=10)

    edgeAC = Edge(from_node=nodeA, to_node=nodeC, distance=20)
    edgeCA = Edge(from_node=nodeC, to_node=nodeA, distance=20)

    edgeBD = Edge(from_node=nodeB, to_node=nodeD, distance=15)
    edgeDB = Edge(from_node=nodeD, to_node=nodeB, distance=15)

    edgeCD = Edge(from_node=nodeC, to_node=nodeD, distance=30)
    edgeDC = Edge(from_node=nodeD, to_node=nodeC, distance=30)

    edgeDE = Edge(from_node=nodeD, to_node=nodeE, distance=10)
    edgeED = Edge(from_node=nodeE, to_node=nodeD, distance=10)

    edgeDG = Edge(from_node=nodeD, to_node=nodeG, distance=10)
    edgeGD = Edge(from_node=nodeG, to_node=nodeD, distance=10)

    edgeEF = Edge(from_node=nodeE, to_node=nodeF, distance=20)
    edgeFE = Edge(from_node=nodeF, to_node=nodeE, distance=20)

    edgeFG = Edge(from_node=nodeF, to_node=nodeG, distance=15)
    edgeGF = Edge(from_node=nodeG, to_node=nodeF, distance=15)

    edgeGJ = Edge(from_node=nodeG, to_node=nodeJ, distance=10)
    edgeJG = Edge(from_node=nodeJ, to_node=nodeG, distance=10)

    edgeDI = Edge(from_node=nodeD, to_node=nodeI, distance=20)
    edgeID = Edge(from_node=nodeI, to_node=nodeD, distance=20)

    edgeCI = Edge(from_node=nodeC, to_node=nodeI, distance=5)
    edgeIC = Edge(from_node=nodeI, to_node=nodeC, distance=5)

    edgeAH = Edge(from_node=nodeA, to_node=nodeH, distance=5)
    edgeHA = Edge(from_node=nodeH, to_node=nodeA, distance=5)

    edgeHI = Edge(from_node=nodeH, to_node=nodeI, distance=10)
    edgeIH = Edge(from_node=nodeI, to_node=nodeH, distance=10)

    topology.add_edge(edgeAB)
    topology.add_edge(edgeBA)

    topology.add_edge(edgeAC)
    topology.add_edge(edgeCA)

    topology.add_edge(edgeBD)
    topology.add_edge(edgeDB)

    topology.add_edge(edgeCD)
    topology.add_edge(edgeDC)

    topology.add_edge(edgeDE)
    topology.add_edge(edgeED)

    topology.add_edge(edgeDG)
    topology.add_edge(edgeGD)

    topology.add_edge(edgeEF)
    topology.add_edge(edgeFE)

    topology.add_edge(edgeFG)
    topology.add_edge(edgeGF)

    topology.add_edge(edgeGJ)
    topology.add_edge(edgeJG)

    topology.add_edge(edgeDI)
    topology.add_edge(edgeID)

    topology.add_edge(edgeCI)
    topology.add_edge(edgeIC)

    topology.add_edge(edgeAH)
    topology.add_edge(edgeHA)

    topology.add_edge(edgeHI)
    topology.add_edge(edgeIH)


def bidding(bids, num_bids, operator, topology):
    for i in range(num_bids):
        bids.append(Bid("client" + str(i), operator, topology))


def auctioning(bids, operator):
    Auction.Auction(bids, operator)
    bids.clear()


def main():

    num_bids = 250
    bids = []
    topology = Graph()

    # Create network topology
    create_network_topology(topology, num_vnf_services=5)

    # Resource advertisement phase
    operator1 = Operator(num_nodes=13, num_links=10, num_vnf_services=5, service_capacity=100, topology=topology)

    # Bidding phase
    bidding(bids=bids, num_bids=num_bids, operator=operator1, topology=topology)

    # Winner determination & price computation phase
    auctioning(bids=bids, operator=operator1)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
