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
from ..common.read_data import FileData
from .dl_job import Dl_Job


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
            for obj in fd.data:
                jb = Dl_Job(obj[0], int(obj[cst_idx]))
                jobs.append(jb)
                # print(jb.name)
        return jobs

    def update_ab(self, job, demand):
        print(job.cost)
        print(job.last_time)
        print(demand.status)
        print(self.a_matrix)

    def start(self):
        print("server running ...")
        while self.running:
            #  Wait for next request from client
            message = self.socket.recv()
            print("Received request: " + str(message.decode()))
            print("running")
            print("checking new demands - allocate to jobs")
            time.sleep(1)
            self.socket.send_string("World from %s" % self.PORT)

