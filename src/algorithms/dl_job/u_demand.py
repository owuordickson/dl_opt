# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""


class Demand:

    def __init__(self, task):
        self.task = task
        self.status = 'incomplete'  # or complete
        self.elapsed_time = -1
