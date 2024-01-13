from aws_data_engineering import DelloDatalakeCommonStackConfiguration

class DelloDatalakeS3BucketsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self):
        super().__init__()

        self.raw_bucket_name = f'dello-datalake-{self.deployment_key}-raw-{self.aws_account_id}-{self.aws_region}'
        self.trusted_bucket_name = f'dello-datalake-{self.deployment_key}-trusted-{self.aws_account_id}-{self.aws_region}'
        self.refined_bucket_name = f'dello-datalake-{self.deployment_key}-refined-{self.aws_account_id}-{self.aws_region}'
        self.utilities_bucket_name = f'dello-datalake-{self.deployment_key}-utilities-{self.aws_account_id}-{self.aws_region}'
