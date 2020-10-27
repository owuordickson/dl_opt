# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import sys
from algorithms.data_lake.dl_client import Dl_Client


def init_client(pt="5556"):
    cli = Dl_Client(pt)
    for req in range(1, 2):
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
