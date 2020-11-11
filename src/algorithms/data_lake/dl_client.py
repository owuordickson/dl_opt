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


class Dl_Client:

    def __init__(self, port):
        self.PORT = port
        context = zmq.Context()
        print("Connecting (client) to server...")
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:%s" % self.PORT)

    def send_req(self, request):
        print("Sending demand ", request, "...")
        self.socket.send_string(request)
        #  Get the reply.
        message = self.socket.recv()
        print("Received reply: ", "[", message.decode(), "]")

