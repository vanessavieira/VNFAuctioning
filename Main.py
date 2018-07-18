from Bid import Bid
from Operator import Operator
from Auction import Auction


def main():

    # Resource advertisement phase
    operator1 = Operator(num_nodes=27, num_links=37, num_vnf_services=3, services_capacity=100)

    # Bidding phase
    bids = []

    for i in range(8):
        bids.append(Bid("client" + str(i), operator1))

    # Winner determination & price computation phase
    auc = Auction(bids)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
