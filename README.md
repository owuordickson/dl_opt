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

* Python

```
$python3 src/init_server.py data/job_cost.csv  
```

To submit jobs:<br>

* 20 is the size of the task (pick any integer number)

```
$python3 src/run_client.py 20 
```