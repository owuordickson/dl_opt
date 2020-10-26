

import sys
import zmq


class Dl_Client:

    def __init__(self, pt):
        self.PORT = pt
        # if len(sys.argv) > 1:
        #    port = sys.argv[1]
        #    int(port)
        context = zmq.Context()
        print("Connecting to server...")
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:%s" % self.PORT)
        # if len(sys.argv) > 2:
        #    socket.connect("tcp://localhost:%s" % port1)

    def send_req(self, request):
        print("Sending request ", request, "...")
        self.socket.send_string("Hello")
        #  Get the reply.
        message = self.socket.recv()
        print("Received reply ", request, "[", message, "]")


def init_client(pt="5556"):
    cli = Dl_Client(pt)
    for req in range(1, 10):
        cli.send_req(req)


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        if len(sys.argv) == 2:
            port = sys.argv[1]
            init_client(port)
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
