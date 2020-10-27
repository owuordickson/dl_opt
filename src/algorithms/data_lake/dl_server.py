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
import random as rand
import string
from multiprocessing import Process
from ..common.read_data import FileData
from .dl_job import Dl_Job
from .u_demand import Demand
from .dl_client import Dl_Client


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
        self.available = np.ones(len(self.jobs), dtype=bool)
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
                jb = Dl_Job(i, name, int(obj[cst_idx]), self.PORT)
                jobs.append(jb)
        return jobs

    def choose_job(self):
        idx = -1
        y = 0
        x = float(rand.randint(1, 10) / 10)
        # print("random: " + str(x))
        # for i in range(len(self.available)):
        for jb in self.jobs:
            if jb.status:  # self.available[i]:
                # idx = i
                idx = jb.index
                a = self.a_matrix[idx]
                cost = 1 / jb.cost
                y = y + (cost * (a / np.sum(self.a_matrix)))
                if y >= x:
                    # return self.jobs[idx]
                    return idx
        return idx

    def update_ab(self, job, end_time):
        elapsed = end_time - job.last_time
        job.last_time = elapsed
        self.a_matrix[job.index] += 1
        print(self.a_matrix)

    def start(self):
        print("server is running ...")
        while self.running:
            #  Wait for next request from client
            temp = self.socket.recv()
            message = temp.decode()
            time.sleep(1)
            # for jb_o in self.jobs:
            #    print(jb_o.status)
            if 'jb' in message:
                # acknowledge job complete and update matrix
                # self.update_ab(jb1, d1)
                end = time.time()
                idx = int(message.strip(string.ascii_letters))
                jb = self.jobs[idx]
                self.update_ab(jb, end)
                jb.status = True  # add to available jobs
                print(str(message) + " (server) updated!")
                self.socket.send_string("ACK")
            else:
                # new user demand
                print("Received demand: " + str(message))
                delay = int(message)
                d1 = Demand(delay)

                print("checking new demands - allocate to jobs")
                jb_idx = self.choose_job()  # jb1 = self.jobs[0]
                if jb_idx == -1:
                    self.socket.send_string("All jobs are busy")
                else:
                    # Now we can connect a client to all the demands
                    # Process(target=self.work, args=([jb_idx, d1],)).start()
                    print("chosen job index: " + str(jb_idx))
                    jb = self.jobs[jb_idx]
                    jb.status = False  # remove from available jobs
                    jb.last_time = time.time()
                    Process(target=jb.work, args=(d1,)).start()

                    self.socket.send_string("Demand allocated to job " + jb.name)
