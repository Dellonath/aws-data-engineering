import os

class CloudFormationStackConfiguration():
    
    def __init__(self):
     
        self.aws_account_id = '975050223655' # os.environ["ACCOUNT_ID"]
        self.aws_region = "us-east-1"
        self.environment = 'dev' # os.environ["ENVIRONMENT"]
        