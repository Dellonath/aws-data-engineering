import os

class CloudFormationStackConfiguration():
    
    def __init__(self):
     
        self.aws_account_id = os.environ["ACCOUNT_ID"]
        self.aws_region = "us-east-1"
        self.environment = os.environ["ENVIRONMENT"]
        