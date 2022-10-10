

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.master('local[*]').appName('this is my spark').getOrCreate()

lst = [1,2,3,4,5]
rdd = spark.sparkContext.parallelize(lst)
rdd.collect()






