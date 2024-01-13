from aws_data_engineering import DelloDatalakeCommonStackConfiguration
from aws_data_engineering.s3.buckets_stack import DelloDatalakeS3BucketsStackConfiguration

class DelloDatalakeGlueJobsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self,
            buckets_stack_configuration: DelloDatalakeS3BucketsStackConfiguration = DelloDatalakeS3BucketsStackConfiguration(),
            **kwargs) -> None:
        super().__init__(**kwargs)
        
        # BUCKETS STACK CONFIGURATION
        self.raw_bucket_name = buckets_stack_configuration.raw_bucket_name
        self.trusted_bucket_name = buckets_stack_configuration.trusted_bucket_name
        self.refined_bucket_name = buckets_stack_configuration.refined_bucket_name
        self.utilities_bucket_name = buckets_stack_configuration.utilities_bucket_name
        
        # IAM
        self.glue_jobs_role_name = f'dello-datalake-{self.deployment_key}-glue-jobs-role'
