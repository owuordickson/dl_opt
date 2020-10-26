

import zmq
import sys


def init_client():
    PORT = "5556"
    # if len(sys.argv) > 1:
    #    port = sys.argv[1]
    #    int(port)
    context = zmq.Context()
    print("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % PORT)
    # if len(sys.argv) > 2:
    #    socket.connect("tcp://localhost:%s" % port1)
    return socket


def send_req(socket):
    #  Do 10 requests, waiting each time for a response
    for request in range(1, 10):
        print("Sending request ", request, "...")
        socket.send("Hello")
        #  Get the reply.
        message = socket.recv()
        print("Received reply ", request, "[", message, "]")


