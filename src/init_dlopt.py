# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@credits: "Anne Laurent"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "26 October 2020"

Usage:
    $python3 init_dlopt.py -f ../data/test_file.csv
Description:
    f -> file path (CSV)

"""

import sys
from optparse import OptionParser
from algorithms.dolpt.dlopt import DlOpt


def init_algorithm(f_path):
    try:
        opt = DlOpt(f_path)
        wr_line = "Algorithm: DL-OPT \n"
        return wr_line
    except Exception as error:
        wr_line = "Failed: " + str(error)
        # print(error)
        return wr_line


def write_file(data, path):
    with open(path, 'w') as f:
        f.write(data)
        f.close()


if __name__ == "__main__":

    if not sys.argv:
        file_path = sys.argv[1]
    else:
        optparser = OptionParser()
        optparser.add_option('-f', '--inputFile',
                             dest='file',
                             help='path to file containing csv',
                             # default=None,
                             default='../data/job_cost.csv',
                             # default='../data/test.csv',
                             type='string')

        (options, args) = optparser.parse_args()
        inFile = None
        if options.file is None:
            print('No data-set filename specified, system with exit')
            print("Usage: $python3 init_dlopt.py -f filename.csv")
            sys.exit('System will exit')
        else:
            inFile = options.file
        file_path = inFile

    import time
    # import tracemalloc

    start = time.time()
    # tracemalloc.start()
    res_text = init_algorithm(file_path)
    # snapshot = tracemalloc.take_snapshot()
    end = time.time()

    wr_text = ("Run-time: " + str(end - start) + " seconds\n")
    # wr_text += (Profile.get_quick_mem_use(snapshot) + "\n")
    wr_text += str(res_text)
    f_name = str('res_dlopt' + str(end).replace('.', '', 1) + '.txt')
    # write_file(wr_text, f_name)
    print(wr_text)
