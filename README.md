# DLOPT: Data Lake Optimization algorithm

### Requirements:
You will be required to install the following python dependencies before using <em><strong>ACO</strong>-GRAANK</em> algorithm:<br>
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

* 20 is the number of tasks to be sent to the server (repetitively after every 0.8 secs) and each task is 20 secs long. Pick any integer to determine the number of tasks
