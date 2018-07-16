from random import randint
from Operator import Operator

class Bid:

    required_service_quantity = []
    valuation = 0

    def __init__(self, client, operator):
        self.client = client
        self.operator = operator
        self.compute_service_quantity()

    def compute_service_quantity(self):
        for j in range(Operator.num_services):
            rand_quantity = randint(1, 30)
            self.required_service_quantity.append(rand_quantity)

    def compute_valuation(self):
        sum_required_service_quantity = 0
        for j in range(len(self.required_service_quantity)):
            sum_required_service_quantity += self.required_service_quantity[j]
        rand_valuation = randint(1, sum_required_service_quantity)
        self.valuation = rand_valuation
