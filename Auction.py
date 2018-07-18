import math


class Auction:

    used_units = []
    winners = []
    prices = []
    sorted_metrics = []

    def __init__(self, bids):
        self.bids = bids
        self.initiate_used_units()
        self.compute_ordered_bids()
        self.compute_winner_bids()
        self.compute_price_for_bids()

    def initiate_used_units(self):
        for j in range(self.bids[0].operator.num_services):
            self.used_units.append(0)

    def compute_ordered_bids(self):
        self.bids.sort(key=lambda x: x.sort_metric, reverse=True)

    def compute_winner_bids(self):
        for i in range(len(self.bids)):
            count_services = 0

            for j in range(self.bids[i].operator.num_services):
                if (self.bids[i].required_service_quantity[j] + self.used_units[j]) <= \
                        self.bids[i].operator.services_capacity:
                    count_services += 1

            if count_services == self.bids[i].operator.num_services:
                for j in range(self.bids[i].operator.num_services):
                    self.used_units[j] += self.bids[i].required_service_quantity[j]

                self.winners.append(self.bids[i])

        for i in range(len(self.winners)):
            print("Winner: " + str(self.winners[i].client))

    def compute_price_for_bids(self):
        for i in range(len(self.winners)):
            count_services = 0
            count_bigger_capacity = 0

            for j in range(self.bids[i].operator.num_services):
                self.used_units[j] = 0

            for k in range(len(self.bids)):
                for j in range(self.bids[k].operator.num_services):
                    if (self.bids[k].required_service_quantity[j] + self.used_units[j]) <= \
                            self.bids[k].operator.services_capacity:
                        count_services += 1

                if count_services == self.bids[k].operator.num_services:
                    for j in range(self.bids[k].operator.num_services):
                        self.used_units[j] += self.bids[k].required_service_quantity[j]

                for j in range(self.bids[k].operator.num_services):
                    if(self.bids[i].required_service_quantity[j] + self.used_units[j]) <= \
                            self.bids[i].operator.services_capacity:
                        count_bigger_capacity += 1

                if count_bigger_capacity > 0:
                    price = self.bids[k].valuation * math.sqrt(self.bids[i].total_required_service_quantity)/\
                            math.sqrt(self.bids[k].total_required_service_quantity)
                    self.prices.append(price)

            print("price: " + str(self.prices[i]))
