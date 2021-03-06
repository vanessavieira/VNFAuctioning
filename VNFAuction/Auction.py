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
        self.bids_unordered = bids
        self.operator = operator
        self.compute_ordered_bids()
        self.compute_winning_bids()
        self.compute_price_for_bids()
        self.compute_metrics()

    def compute_ordered_bids(self):
        self.bids.sort(key=lambda x: x.sort_metric, reverse=True)
        for i in range(len(self.bids)):
            print(self.bids[i].client)

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
            print("Winner: " + str(self.winners[i].client) + "; valuation: " + str(self.winners[i].valuation))

        print("\n")

    def compute_price_for_bids(self):
        self.services = self.operator.services

        for winner in self.winners:
            winner.price_to_pay = winner.valuation

        for i in range(len(self.winners)):

            for j in range(len(self.services)):
                self.services[j].used_units = 0

            # Auction without winner i

            for k in range(len(self.bids)):
                count_services = 0
                count_bigger_capacity = 0

                # print("k: " + str(k) + " i:" + str(i))

                if self.bids[k] == self.winners[i]:
                    continue

                num_services = len(self.bids[k].required_services)

                for service in range(num_services):
                    if self.bids[k].required_service_quantity[service] +\
                            self.bids[k].required_services[service].used_units\
                            <= self.bids[k].operator.service_capacity:
                        count_services += 1

                if count_services == num_services:
                    for service in range(num_services):
                        self.bids[k].required_services[service].used_units += \
                            self.bids[k].required_service_quantity[service]

                # print("bid i: " + str(self.winners[i].required_service_quantity))
                # print("bid k: " + str(self.bids[k].required_service_quantity))
                # print("\n")

                for j in range(len(self.winners[i].required_services)):
                    if self.winners[i].required_service_quantity[j] + self.winners[i].required_services[j].used_units >= \
                            self.winners[i].operator.service_capacity:
                        count_bigger_capacity += 1

                        price = (self.bids[k].valuation * math.sqrt(self.winners[i].total_required_service_quantity)) / \
                                math.sqrt(self.bids[k].total_required_service_quantity)

                        self.winners[i].price_to_pay = price

                        #print("winner: " + str(self.winners[i].client) + "; ordem i: " + str(i) + "; ordem k: " + str(k))

                        self.prices.append(price)
                        break

                if count_bigger_capacity > 0:
                    break

        print("\n")
        for i in range(len(self.winners)):
            print("Price " + str(self.winners[i].client) + ": " + str(self.winners[i].price_to_pay))
            # print("price: " + str(self.prices[i]))

    def compute_metrics(self):
        self.num_bids = len(self.bids)
        self.service_capacity = self.operator.service_capacity
        self.accepted_bids = len(self.winners)
        self.accepted_bids_percentage = (self.accepted_bids / self.num_bids) * 100
        total_valuation = 0

        print("\nprice size: " + str(len(self.prices)))

        for i in range(self.num_bids):
            total_valuation += self.bids[i].valuation

        for j in range(len(self.winners)):
            self.market_valuation += self.winners[j].valuation
            self.operator_revenue += self.winners[j].price_to_pay

        self.mean_bid_price = self.operator_revenue / self.accepted_bids

        print("\nNum Bids = " + str(self.num_bids))
        print("Accepted Bids = " + str(self.accepted_bids))
        print("Market Valuation = " + str(self.market_valuation))
        print("Operator Revenue = " + str(self.operator_revenue))
        print("Percentage of Accepted Bids = " + str(self.accepted_bids_percentage))
        print("Service Capacity = " + str(self.service_capacity))
        print("Mean Bid Price = " + str(self.mean_bid_price))





