# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import time
from .dl_client import Dl_Client


class Dl_Job(Dl_Client):

    def __init__(self, index, name, cost, port, mem=None, cpus=None):
        self.index = index
        self.port = port
        self.name = name
        self.cost = cost  # specs
        self.status = True
        self.running = True
        self.demands = []
        self.last_time = -1
        # self.mem_size = mem
        # self.cpus = cpus
        # self.cost = self.calculate_cost()

    # def calculate_cost(self):
    #    cost = self.cpus + self.mem_size
    #    return cost

    def work(self, demand):
        super().__init__(self.port)
        start = time.time()
        if demand.status is 'incomplete':
            # initiate task
            self.demands.append(demand)
            self.run()
        end = time.time()
        self.last_time = (end - start)
        print(str(self.name) + " (client) completed work ...")
        self.socket.send_string(self.name)
        #  Get the reply.
        temp = self.socket.recv()
        print(str(self.name) + " (client) " + str(temp.decode()) + " & disconnected")

    def run(self):
        print(str(self.name) + " (client) starting work ...")
        # do work
        demand = self.demands[-1]  # last item to be stored
        delay = demand.task  # in seconds
        time.sleep(delay)
        demand.status = 'complete'

