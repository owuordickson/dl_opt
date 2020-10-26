# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

Description: greedy heuristic algorithm that optimizes data lake jobs

"""

import numpy as np
import time
from .daemon import Daemon
from ..common.read_data import FileData
from ..dl_job.dl_job import Dl_Job


class DlOpt(Daemon):

    def __init__(self, file):
        self.jobs = self.init_jobs(file)
        self.a_matrix = np.ones(len(self.jobs), dtype=float)
        print(self.a_matrix)
        # self.demands = np.array([])  # to be sent randomly
        # self.cost_matrix = np.array([])
        # self.job_status = np.array([])

    def init_jobs(self, file_path):
        jobs = []
        cst_idx = -1
        fd = FileData(file_path)
        for k, v in fd.title:
            # print(str(k) + ' ' + str(v.decode()))
            if v.decode() == 'cost':
                cst_idx = k
        if cst_idx > 0:
            # print(fd.data)
            for obj in fd.data:
                jb = Dl_Job(obj[0], int(obj[cst_idx]))
                jobs.append(jb)
                print(jb.name)
        return jobs

    def update_ab(self):
        print(self.a_matrix)

    def run(self):
        while True:
            print("running")
            time.sleep(1)

# class DlService(Daemon):  # to be removed
#    def run(self):  # implemented in DlOpt
        # Or simply merge your code with MyDaemon.
#        your_code = DlOpt()
#        your_code.run()
