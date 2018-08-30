import math


class Auction:
    used_units = []
    winners = []
    prices = []
    sorted_metrics = []
    services = []

    # for metrics computation
    num_bids = 0
    market_valuation = 0
    operator_revenue = 0
    accepted_bids = 0
    service_capacity = 0
    mean_bid_price = 0
    accepted_bids_percentage = 0

    def __init__(self, bids, operator):
        self.bids = bids
        self.operator = operator
        self.compute_ordered_bids()
        self.compute_winning_bids()
        self.compute_price_for_bids()
        self.compute_metrics()

    def compute_ordered_bids(self):
        self.bids.sort(key=lambda x: x.sort_metric, reverse=True)

    def compute_winning_bids(self):

        for i in range(len(self.bids)):
            num_services = len(self.bids[i].required_services)

            count_services = 0
            for j in range(num_services):
                if (self.bids[i].required_service_quantity[j] + self.bids[i].required_services[j].used_units) \
                        <= self.bids[i].operator.service_capacity:
                    count_services += 1

            if count_services == num_services:
                self.winners.append(self.bids[i])

                for j in range(num_services):
                    self.bids[i].required_services[j].used_units += self.bids[i].required_service_quantity[j]

        for i in range(len(self.winners)):
            print("Winner: " + str(self.winners[i].client))

        print("\n")

    def compute_price_for_bids(self):
        self.services = self.operator.services

        for j in range(len(self.services)):
            self.services[j].used_units = 0

        for i in range(len(self.winners)):
            count_services = 0
            count_bigger_capacity = 0

            for k in range(len(self.bids)):
                num_services = len(self.bids[k].required_services)

                for j in range(num_services):
                    if (self.bids[k].required_service_quantity[j] + self.bids[k].required_services[j].used_units)\
                            <= self.bids[k].operator.service_capacity:
                        count_services += 1

                if count_services == num_services:
                    for j in range(num_services):
                        self.bids[k].required_services[j].used_units += self.bids[k].required_service_quantity[j]

                for j in range(len(self.bids[i].required_services)):
                    if(self.bids[i].required_service_quantity[j] + self.bids[i].required_services[j].used_units) <= \
                            self.bids[i].operator.service_capacity:
                        count_bigger_capacity += 1

                if count_bigger_capacity > 0:
                    price = self.bids[k].valuation * math.sqrt(self.bids[i].total_required_service_quantity)/\
                            math.sqrt(self.bids[k].total_required_service_quantity)
                    self.prices.append(price)

            print("price: " + str(self.prices[i]))

    def compute_metrics(self):
        self.num_bids = len(self.bids)
        self.service_capacity = self.operator.service_capacity
        self.accepted_bids = len(self.winners)
        self.accepted_bids_percentage = (self.accepted_bids / self.num_bids) * 100

        for i in range(self.num_bids):
            self.market_valuation += self.bids[i].valuation

        for j in range(len(self.winners)):
            self.operator_revenue += self.prices[j]

        self.mean_bid_price = self.market_valuation / self.num_bids

        print("\nNum Bids = " + str(self.num_bids))
        print("Service Capacity = " + str(self.service_capacity))
        print("Accepted Bids = " + str(self.accepted_bids))
        print("Market Valuation = " + str(self.market_valuation))
        print("Operator Revenue = " + str(self.operator_revenue))
        print("Mean Bid Price = " + str(self.mean_bid_price))





