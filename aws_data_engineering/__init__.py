import os

class DelloDatalakeCommonStackConfiguration():
    
    def __init__(self, **kwargs):

        self.aws_account_id = os.environ["CDK_DEFAULT_ACCOUNT"]
        self.aws_region = os.environ["CDK_DEFAULT_REGION"]
        self.deployment_key = os.environ["ENVIRONMENT"]
