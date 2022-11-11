import pyspark
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import StringType, StructField, StructType

c1 = StructType([StructField('Name',StringType(),True),StructField('Profession',StringType(),True) , StructField('Location',StringType(), True)])
df = spark.createDataFrame(data1,c1)
df.show()