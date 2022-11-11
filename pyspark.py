from pyspark.sql import SparkSession


df_books = spark.read.parquet("s3://amazon-reviews-pds/parquet/product_category=Books/part-00000-495c48e6-96d6-4650-aa65-3c36a3516ddd.c000.snappy.parquet")
df_books.createOrReplaceTempView("tbl_books")
