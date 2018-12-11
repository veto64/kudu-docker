# Debian based Docker image for Kudu with 3 slaves

The main repository is on:
[https://calantas.org/kudu-docker/](https://calantas.org/kudu-docker)

![logo](http://getkudu.io/img/logo.png)

## License
GNU General Public License v3.0 -

## What is Kudu?
Kudu is an open source storage engine for structured data which supports low-latency random access together with effi- cient analytical access patterns. Kudu distributes data using horizontal partitioning and replicates each partition using Raft consensus, providing low mean-time-to-recovery and low tail latencies. Kudu is designed within the context of the Hadoop ecosystem and supports many modes of access via tools such as [Cloudera Impala](http://impala.io/), [Apache Spark](http://spark.apache.org/), and [MapReduce](https://hadoop.apache.org/).

[http://kudu.apache.org/](http://kudu.apache.org/)

## Dockers
### There are 3 kudu dockers:
1. veto64/kudu-docker:14 (old kudu version 14)
2. veto64/kudu-docker:latest (the latest from the git source repository)
3. veto64/kudu-docker:api (REST API, to interact with kudu engine, based on the python API framework Falcon)

## Usage
Check the docker-compose.yml files

example inside the folder api:
```Bash
docker-compose up -d







### Web UI
| Control Websiste               | Port                                              |
| ----------------------- |-------------------------------------------------- |
| Landing                 | [http://127.0.0.1:8051](http://127.0.0.1:8051)  |
| View Slaves/Tablets     | [http://127.0.0.1:8051/tablet-servers](http://127.0.0.1:8051/tablet-servers)  |



