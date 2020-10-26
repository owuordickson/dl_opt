# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

Description: greedy heuristic algorithm that optimizes data lake jobs

"""

import sys
import zmq


class Dl_Client:

    def __init__(self, port):
        self.PORT = port
        context = zmq.Context()
        print("Connecting to server...")
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:%s" % self.PORT)

    def send_req(self, request):
        print("Sending request ", request, "...")
        self.socket.send_string("Hello")
        #  Get the reply.
        message = self.socket.recv()
        print("Received reply ", request, "[", message.decode(), "]")


def init_client(pt="5556"):
    cli = Dl_Client(pt)
    for req in range(1, 10):
        cli.send_req(req)


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        if len(sys.argv) == 2:
            prt = sys.argv[1]
            init_client(prt)
        else:
            init_client()

        # if 'start' == sys.argv[1]:
        #    server.start()
        # else:
        #    print("Unknown command")
        #    sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s ..." % sys.argv[0])
        sys.exit(2)
