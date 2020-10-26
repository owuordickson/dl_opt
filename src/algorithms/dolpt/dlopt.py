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


class DlOpt:

    def __init__(self):
        self.jobs = np.array([])
        self.demands = np.array([])
        self.a_matrix = np.array([])
        self.cost_matrix = np.array([])

    def run(self):
        while True:
            print("running")
            time.sleep(1)


class DlService(Daemon):
    def run(self):
        # Or simply merge your code with MyDaemon.
        your_code = DlOpt()
        your_code.run()
