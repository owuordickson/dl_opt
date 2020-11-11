# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import sys
import time
import random as rand
from algorithms.data_lake.dl_client import Dl_Client


def init_client(n, port="5556"):
    cli = Dl_Client(port)
    # cli.send_req(dl)
    dl = "20"
    for i in range(int(n)):
        cli.send_req(dl)
        x = float(rand.randint(1, 4) / 100)
        w = x * float(dl)
        time.sleep(w)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if len(sys.argv) == 3:
            size = sys.argv[1]
            prt = sys.argv[2]
            init_client(size, prt)
        else:
            size = sys.argv[1]
            start = time.time()
            init_client(size)
            end = time.time()
            print("Elapsed time: " + str(end - start))
        # if 'start' == sys.argv[1]:
        #    server.start()
        # else:
        #    print("Unknown command")
        #    sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s delay port" % sys.argv[0])
        sys.exit(2)
