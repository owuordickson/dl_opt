

import zmq
import time
import sys


class Dl_Server:

    def __init__(self, port="5556"):
        self.PORT = port
        self.running = True
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % self.PORT)
        print("server initialized")

    def start(self):
        print("server running ...")
        while self.running:
            #  Wait for next request from client
            message = self.socket.recv()
            print("Received request: " + str(message))
            time.sleep(1)
            self.socket.send_string("World from %s" % self.PORT)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if len(sys.argv) == 3:
            prt = sys.argv[2]
            server = Dl_Server(prt)
        else:
            server = Dl_Server()
        if 'start' == sys.argv[1]:
            server.start()
        # elif 'stop' == sys.argv[1]:
        #    server.stop()
        # elif 'restart' == sys.argv[1]:
        #    server.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
