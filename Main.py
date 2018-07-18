from Bid import Bid
from Operator import Operator
from Auction import Auction



def main():
    # Resource advertisement phase

    operator1 = Operator(3, 2, 2, 10)

    # Bidding phase
    bids = []
    bid1 = Bid("client1", operator1)
    bids.append(bid1)

    bid2 = Bid("client2", operator1)
    bids.append(bid2)

    # Winner determination phase
    auc = Auction(bids)

    # Price computation phase

    # VNF instantiation phase

if __name__ == "__main__":
    main()
