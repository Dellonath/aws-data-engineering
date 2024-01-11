from aws_data_engineering import DelloDatalakeCommonStackConfiguration

class DelloDatalakeGlueJobsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self):
        super().__init__()
        
        # IAM
        self.glue_jobs_role_name = 'dello-datalake-glue-jobs-role'
        
        # GLUE
        self.raw_to_trusted_job_name = 'dellotech-datalake-raw-to-trusted-job'
        self.trusted_to_refined_job_name = 'dellotech-datalake-raw-to-trusted-job'
        self.jobs_tags = {
            'owner': 'dellonath@gmail.com',
            'company': 'dellotech consulting',
            'project': 'aws-data-engineering'
        }
    