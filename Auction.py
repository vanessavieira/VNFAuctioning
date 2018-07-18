import numpy as np
from Operator import Operator

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
        # self.compute_price_for_bids()

    def initiate_used_units(self):
        for j in range(self.bids[0].operator.num_services):
            self.used_units.append(0)

    def compute_ordered_bids(self):
        self.bids.sort(key=lambda x: x.sort_metric, reverse=True)

        for n in range(len(self.bids)):
            print(self.bids[n].sort_metric)

    def compute_winner_bids(self):
        for i in range(len(self.bids)):
            count_services = 0

            for j in range(self.bids[i].operator.num_services):
                if (self.bids[i].required_service_quantity[j] + self.used_units[j]) <= self.bids[i].operator.services_capacity:
                    count_services += 1

            if count_services == self.bids[i].operator.num_services:
                for j in range(self.bids[i].operator.num_services):
                    self.used_units[j] += self.bids[i].required_service_quantity[j]

                self.winners.append(self.bids[i])

    #def compute_price_for_bids(self):