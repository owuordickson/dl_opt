# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import time
from .u_demand import Demand


class Dl_Job:

    def __init__(self, name, cost, mem=None, cpus=None):
        self.name = name
        # self.mem_size = mem
        # self.cpus = cpus
        # self.cost = self.calculate_cost()
        self.cost = cost
        self.status = True

    # def calculate_cost(self):
    #    cost = self.cpus + self.mem_size
    #    return cost

    def work(self, demand):
        self.status = False
        delay = demand.task  # in seconds
        time.sleep(delay)
        self.status = True
