import datetime
import logging
import sys

from random import shuffle


logger = logging.getLogger(__name__)


def run_spark(args):
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StringType, StructField, StructType

    timestamp = str(datetime.datetime.now()).replace(" ", "_")

    spark = SparkSession.builder.appName(f"Task_{timestamp}").getOrCreate()
    sc = spark.sparkContext

    chopped = []

    vegg = sc.textFile(args[1]).collect()
    logger.info(f'Got {",".join(vegg)}. Start Chopping.'.replace("\n", ""))

    for line in vegg:
        chopped.extend(list(line.rstrip()))

    shuffle(chopped)

    result = "".join(chopped)
    logger.info(f"Chopped vegetables:{result}")

    fields = [StructField("salad", StringType(), True)]
    schema = StructType(fields)

    df = spark.createDataFrame([(result,)], schema)
    df.coalesce(1).write.csv(args[2])
    sc.stop()


if __name__ == "__main__":
    run_spark(sys.argv)
