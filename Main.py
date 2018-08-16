from Bid import Bid
from Operator import Operator
from Auction import Auction

def bidding(bids, num_bids, operator):
    for i in range(num_bids):
        bids.append(Bid("client" + str(i), operator))


def auctioning(bids, operator):
    auc = Auction(bids, operator)
    bids.clear()


def main():
    num_bids = 100
    bids = []

    # Resource advertisement phase
    operator1 = Operator(num_nodes=27, num_links=37, num_vnf_services=5, service_capacity=100)

    # Bidding phase
    bidding(bids=bids, num_bids=num_bids, operator=operator1)

    # Winner determination & price computation phase
    auctioning(bids=bids, operator=operator1)

    # VNF instantiation phase

if __name__ == "__main__":
    main()
