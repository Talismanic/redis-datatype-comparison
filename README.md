# redis-datatype-comparison
Comparing different data type of redis
Here we compared the speed of insertion and retrieval of 3 three different type of data in Redis. We have not used pipelining intentionally to measure the actual unoptimized scenario.

|Type                     |used_memory | used_rss | total_insertion_time |avg_read_time/key |
|-------------------------|------------|----------|----------------------|------------------|
|1M data in Hash Data Type|368MB|368MB|23min| 2ms -4ms|
|1M data in ZSET| 368MB | 375MB | 22min | 4ms to 10ms |
|1M data in string| 429MB | 438MB | 28min | 6ms t0 13ms|


So it seems that to Hash data type takes a little bit of higher time than the ZSET, it is often much more faster while reading the data. Apart from that, complexity O(n) of the oprations related to the datatypes needs to be kept in mind when designing the use cases.
