# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import time
from ..common.daemon import Daemon
from .dl_client import Dl_Client
from .u_demand import Demand


class Dl_Job(Dl_Client):

    def __init__(self, name, cost, port, mem=None, cpus=None):
        # super().__init__(port)
        # self.pidfile = '/tmp/daemon-job' + str(name) + '.pid'
        self.port = port
        self.name = name
        self.cost = cost
        self.status = True
        self.running = True
        self.demands = []
        self.last_time = -1
        # super().__init__(self.pidfile)
        # self.mem_size = mem
        # self.cpus = cpus
        # self.cost = self.calculate_cost()

    # def calculate_cost(self):
    #    cost = self.cpus + self.mem_size
    #    return cost

    # def initiate(self):
    #    while self.running:
            #  Wait for next request from client
    #        temp = self.socket.recv()
    #        msg = temp.decode()

    def work(self, demand):
        super().__init__(self.port)
        start = time.time()
        if demand.status is 'incomplete':
            self.status = False
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
        self.status = True

