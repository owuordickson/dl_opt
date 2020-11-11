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
from algorithms.data_lake.dl_client import Dl_Client


def init_client(dl, port="5556"):
    cli = Dl_Client(port)
    # cli.send_req(dl)
    w = 0.1 * float(dl)
    for i in range(100):
        cli.send_req(dl)
        time.sleep(w)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if len(sys.argv) == 3:
            delay = sys.argv[1]
            prt = sys.argv[2]
            init_client(delay, prt)
        else:
            delay = sys.argv[1]
            init_client(delay)
        # if 'start' == sys.argv[1]:
        #    server.start()
        # else:
        #    print("Unknown command")
        #    sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s delay port" % sys.argv[0])
        sys.exit(2)
