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
        
        # IAM
        self.glue_jobs_role_name = f'{self.project_prefix}-{self.environment}-glue-jobs-role'
        
        # GLUE
        self.raw_to_trusted_job_name = f'{self.project_prefix}-{self.environment}-raw-to-trusted-job'
        self.trusted_to_refined_job_name = f'{self.project_prefix}-{self.environment}-trusted-to-refined-job'
        self.jobs_tags = {
            'owner': 'dellonath@gmail.com',
            'company': 'dellotech consulting',
            'project': 'aws-data-engineering',
            'environment': self.environment
        }
        