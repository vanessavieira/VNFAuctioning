from random import randint
import math

class Bid:

    required_service_quantity = []
    total_required_service_quantity = 0
    valuation = 0
    sort_metric = 0

    def __init__(self, client, operator):
        self.client = client
        self.operator = operator
        self.compute_service_quantity()
        self.compute_valuation()
        self.compute_sort_metric()

    def compute_service_quantity(self):
        for j in range(self.operator.num_services):
            rand_quantity = randint(1, self.operator.services_capacity)
            self.total_required_service_quantity += rand_quantity
            self.required_service_quantity.append(rand_quantity)

        print(self.required_service_quantity)
        print(self.total_required_service_quantity)

    def compute_valuation(self):
        rand_valuation = randint(1, self.total_required_service_quantity)
        self.valuation = rand_valuation

        print(self.valuation)

    def compute_sort_metric(self):
        self.sort_metric = self.valuation/(math.sqrt(self.total_required_service_quantity))

        print(self.sort_metric)
