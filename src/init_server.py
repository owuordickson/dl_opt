# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

"""

import sys
from algorithms.data_lake.dl_server import Dl_Server

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        jb_file = sys.argv[1]
        if len(sys.argv) == 3:
            prt = sys.argv[2]
            server = Dl_Server(jb_file, prt)
        else:
            server = Dl_Server(jb_file)
        server.start()
        # if 'start' == sys.argv[1]:
        #    server.start()
        # elif 'stop' == sys.argv[1]:
        #    server.stop()
        # elif 'restart' == sys.argv[1]:
        #    server.restart()
        # else:
        #    print("Unknown command")
        #    sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s job_file port" % sys.argv[0])
        sys.exit(2)