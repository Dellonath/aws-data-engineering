import sys
from pyspark.sql import DataFrame
from pyspark.context import SparkContext
from collections.abc import Sequence, Mapping
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

def get_job_arguments(required: Sequence[str]) -> Mapping[str, str]:
    
    args = getResolvedOptions(
        sys.argv, 
        required
    )

    return args

if __name__ == '__main__':
    
    args = get_job_arguments(
        required = [
            'JOB_NAME',
            '--RAW_PATH',
            '--TRUSTED_PATH',
            '--RAW_TYPE',
            '--FULL_LOAD'
        ]
    )
    
    raw_dataframe = (
        spark.read
        .format(args.get('--RAW_TYPE'))
        .option('header', 'true')
        .load(args.get('--RAW_PATH'))
    )
    

    dataFrame.write\
        .format("csv")\
        .option("quote", None)\
        .mode("append")\
        .save("s3://s3path")
        
        
        
# Sample Script
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "database",
    table_name = "relatedqueries_csv",
    transformation_ctx = "datasource0"
)

applymapping1 = ApplyMapping.apply(
    frame = datasource0,
    mappings = [("col0", "string", "name", "string"), ("col1", "string", "number", "string")],
    transformation_ctx = "applymapping1"
)

datasink2 = glueContext.write_dynamic_frame.from_options(
    frame = applymapping1,
    connection_type = "s3",
    connection_options = {"path": "s3://input_path"},
    format = "json",
    transformation_ctx = "datasink2"
)


job.commit()