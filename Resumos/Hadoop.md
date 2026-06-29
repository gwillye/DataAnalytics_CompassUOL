# Learn by Example: Hadoop, MapReduce for Big Data problems

## Seção 1 - Introduction

## Seção 2 - Why is Big Data a Big Deal

### The Big Data Paradigm

A review about Big Data. For more information, read the abstract of the course "Fundamentos Big Data 3.0" in [this link](https://gabrielwillye.notion.site/Fundamentos-de-Big-Data-79a06f2c95214628a5e1a884cb6ce161?pvs=4).

### Serial vs Distributed Computing

When the data lives in a single location, the transfer speed and the read speed are slow. To solve that, you can distribute the data across many locations and process it in parallel. Distributed Computing ends up being faster than Serial Computing. On top of that, in Serial Computing the data size is limited by the disk size, while in Distributed Computing the data size is basically unlimited. That has a direct impact on price too, so Distributed Computing tends to be cheaper than Serial Computing.

### What is Hadoop?

A few definitions to set the ground:

**Hadoop** is a distributed computing framework developed by Apache and written in Java.

**HDFS** is a file system to manage the storage of data (Hadoop Distributed File System).

**MapReduce** is a framework to process data across multiple servers.

So, in short, Hadoop is HDFS + MapReduce. Hadoop is actually an open source implementation of two proprietary technologies by Google:

* GFS (Google File System)
* MapReduce, a framework to process data across multiple servers

Going a bit further:

**YARN** is a framework to RUN the data processing task.

**MapReduce** is a framework to DEFINE a data processing task.

Putting it all together: Hadoop = HDFS + YARN + MapReduce.

### HDFS or the Hadoop Distributed File System

Hadoop uses HDFS to store data across multiple disks. Hadoop is normally deployed on a group of machines (a Cluster), and each machine in the cluster is a node. One of these nodes acts as the master node, and it manages the overall file system. The name node stores the directory structure and the metadata for all the files. The other nodes are called data nodes, and the data is physically stored on them.

The file is broken into blocks of 128 MB. That size is chosen to minimize the time to seek to the block on the disk. The name node stores the block locations for each file.

![Example picture](https://snipboard.io/zmSBRK.jpg)

One of the challenges in Distributed Computing is what happens if a block or a data node gets corrupted. To solve that, you can define a replication factor in HDFS: each block is replicated, and the replicas are stored in different data nodes.

![Example picture](https://snipboard.io/u4Obi8.jpg)

### MapReduce Introduced

Let's say we stored a text file in HDFS. The file is made of blocks stored on different nodes, and the goal is to find how many times the word "hello" shows up in the file. There are two ways to do it.

#### Option 1

1. Reconstruct the complete file in one node.
2. Process the file to count the number of "hello"s.

Pro: this program is relatively simple to write.
Con: we are not taking advantage of the parallelism inherent in Hadoop.

#### Option 2

1. Process each block in the node where it is stored (each result is the number of "hello"s in that block).
2. Take all the results to one node and combine them. The answer is simply the sum of all the results.

This is exactly the idea behind MapReduce. MapReduce is a way to parallelize a data processing task.

#### Map Phase

1. Process each block in the node where it is stored.
2. Take all the results to one node and combine them.

Distributed computing can get very complicated, with resources and memory to manage across many nodes. MapReduce abstracts the programmer away from all of that. You just define two functions, and Hadoop takes care of the rest: map() and reduce().

The advantage of using Hadoop is the parallelization you get by expressing any task as map + reduce tasks.

### YARN or Yet Another Resource Navigator

YARN was introduced in Hadoop 2.0 to handle resource management separately. YARN takes care of managing the resources on the Hadoop cluster. It coordinates all the different MapReduce tasks running on the cluster, and it also monitors for failures and assigns new nodes when others fail.

### Resume of the step-by-step of Hadoop

**MapReduce**: the user defines map and reduce tasks using the MapReduce API.

**YARN**: a job is triggered on the cluster.

**HDFS**: YARN figures out where and how to run the job, and stores the result in HDFS.

## The MapReduce "HelloWorld"

The key insight of the paradigm is this: ANY data processing task can be parallelized if you express it as

<key, value> -> map() -> <key, value> -> reduce() -> <key, value>

That is, a map() task that transforms a <key, value> pair into a set of <key, value> pairs, and a reduce() task that combines values which share the same key.

A classic example: you have a large text file and the goal is to create a frequency distribution of the words in it. This is a common task in Natural Language Processing.
