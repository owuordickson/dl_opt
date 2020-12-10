# DLOPT: Data Lake Optimization algorithm

A greedy heuristic algorithm that optimizes data lake jobs.

### Requirements:
You will be required to install the following python dependencies before using <em><strong>DL-OPT</strong></em> algorithm:<br>
```
                   install python (version => 3.6)

```

```
                    $ pip3 install numpy pyzmq setuptools

```

### Usage:
Use it a command line program with the local package:<br>
To start server:<br>

```
$python3 src/init_server.py data/job_cost.csv  
```

To submit jobs (open another command line to run):<br>

```
$python3 src/run_client.py 20 
```

* 20 is the number of tasks to be sent to the server (that occur randomly between every 0.2 - 1.0 secs) and each task is 20 secs long. Pick any integer to determine the number of tasks
