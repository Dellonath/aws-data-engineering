import os

class DelloDatalakeCommonStackConfiguration():
    
    def __init__(self):

        self.aws_account_id = os.environ["CDK_DEFAULT_ACCOUNT"]
        self.aws_region = os.environ["CDK_DEFAULT_REGION"]
        self.environment = os.environ["ENVIRONMENT"]
        self.project_prefix = "dello-datalake"