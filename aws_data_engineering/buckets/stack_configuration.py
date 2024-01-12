from aws_data_engineering import DelloDatalakeCommonStackConfiguration

class DelloDatalakeBucketsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self):
        super().__init__()

        self.raw_bucket_name = f'{self.project_prefix}-{self.environment}-raw-{self.aws_account_id}-{self.aws_region}'
        self.trusted_bucket_name = f'{self.project_prefix}-{self.environment}-trusted-{self.aws_account_id}-{self.aws_region}'
        self.refined_bucket_name = f'{self.project_prefix}-{self.environment}-refined-{self.aws_account_id}-{self.aws_region}'
        self.utilities_bucket_name = f'{self.project_prefix}-{self.environment}-utilities-{self.aws_account_id}-{self.aws_region}'
     