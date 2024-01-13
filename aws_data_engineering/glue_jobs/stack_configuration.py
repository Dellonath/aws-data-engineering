from aws_data_engineering import DelloDatalakeCommonStackConfiguration
from aws_data_engineering.buckets.buckets_stack import DelloDatalakeBucketsStackConfiguration

class DelloDatalakeGlueJobsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self,
            buckets_stack_configuration: DelloDatalakeBucketsStackConfiguration = DelloDatalakeBucketsStackConfiguration(),
            **kwargs) -> None:
        super().__init__(**kwargs)
        
        # BUCKETS STACK CONFIGURATION
        self.raw_bucket_name = buckets_stack_configuration.raw_bucket_name
        self.trusted_bucket_name = buckets_stack_configuration.trusted_bucket_name
        self.refined_bucket_name = buckets_stack_configuration.refined_bucket_name
        self.utilities_bucket_name = buckets_stack_configuration.utilities_bucket_name
        
        # IAM
        self.glue_jobs_role_name = f'dello-datalake-{self.deployment_key}-glue-jobs-role'
        
