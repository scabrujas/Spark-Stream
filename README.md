# Spark-Stream

#### Steps to Execute :

1. Start the server on the Workspace:
   - On terminal run `/usr/bin/zookeeper-server-start config/zookeeper.properties`
   - On a separeate terminal run `/usr/bin/kafka-server-start config/server.properties`

2. Install packages:
    - run `./start.sh` to install requirements from requirements.txt

3. Run producer and check the kafka-console-consumer:
    - Run `python kafka_server.py` 
    - On a separe terminal check the data, run `kafka-console-consumer --bootstrap-server localhost:9092 --topic police.service.calls --from-beginning`   
   
   Output will be:
   <img src='https://github.com/scabrujas/Spark-Stream/blob/master/console_consumer.png'/>

5. Run consumer:
    - Run `python consumer_server.py`
   
   Output will be:
   <img src='https://github.com/scabrujas/Spark-Stream/blob/master/consumer_server.png'/>

6. Run Streaming Application:
     - Run `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`
   
   Output will be:
   <img src='https://github.com/scabrujas/Spark-Stream/blob/master/spark.png'/>


Answer to the questions:

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

    spark.executor.memory : setting executor memory 
    spark.executor.cores : setting executor cores
    spark.driver.memory : setting driver memory
    numInputRecords : The number of records processed in a trigger
    inputRowsPerSecond : The rate of data arriving
    processedRowsPerSecond : The rate at which Spark is processing data
    

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal? 

    spark.default.parallelism : 3
    spark.streaming.kafka.maxRatePerPartition : 10
