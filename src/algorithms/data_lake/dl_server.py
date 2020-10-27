# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

Description: greedy heuristic algorithm that optimizes data lake jobs

"""

import zmq
import time
import numpy as np
from  multiprocessing import Process
from ..common.read_data import FileData
from .dl_job import Dl_Job
from .u_demand import Demand


class Dl_Server:

    def __init__(self, file, port="5556"):
        self.PORT = port
        self.file_path = file
        self.running = True
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % self.PORT)
        print("server initialized ...")
        self.jobs = self.init_jobs()
        self.a_matrix = np.ones(len(self.jobs), dtype=float)
        print(str(len(self.jobs)) + " jobs created ...")

    def init_jobs(self):
        jobs = []
        cst_idx = -1
        fd = FileData(self.file_path)
        for k, v in fd.title:
            # print(str(k) + ' ' + str(v.decode()))
            if v.decode() == 'cost':
                cst_idx = k
        if cst_idx > 0:
            # print(fd.data)
            for i in range(len(fd.data)):
                obj = fd.data[i]
                name = 'jb' + str(i)
                jb = Dl_Job(name, int(obj[cst_idx]), self.PORT)
                jobs.append(jb)
        return jobs

    def update_ab(self, job, demand):
        print(job.cost)
        print(job.last_time)
        print(demand.status)
        print(self.a_matrix)

    def start(self):
        print("server is running ...")
        while self.running:
            #  Wait for next request from client
            temp = self.socket.recv()
            message = temp.decode()
            time.sleep(1)
            if 'jb' in message:
                # acknowledge job complete and update matrix
                # self.update_ab(jb1, d1)
                print(str(message) + " (server) updated!")
                self.socket.send_string("ACK")
            else:
                # new user demand
                print("Received demand: " + str(message))
                delay = int(message)
                d1 = Demand(delay)

                print("checking new demands - allocate to jobs")
                # Now we can connect a client to all the demands
                # Process(target=jb1.work, args=([d1],)).start()
                jb1 = self.jobs[0]
                Process(target=jb1.work, args=(d1,)).start()

                self.socket.send_string("World from %s" % self.PORT)

