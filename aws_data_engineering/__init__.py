import os
import json

class DelloDatalakeCommonStackConfiguration():
    
    def __init__(self, **kwargs):

        self.aws_account_id = os.environ["CDK_DEFAULT_ACCOUNT"]
        self.aws_region = os.environ["CDK_DEFAULT_REGION"]
        self.deployment_key = os.environ["ENVIRONMENT"]
        
    def _attribute_variables(self, config: dict) -> dict:
    
        yaml_configs_str = (f'{json.dumps(config)}'
            .replace('{aws_account_id}', self.aws_account_id)
            .replace('{aws_region}', self.aws_region)
            .replace('{deployment_key}', self.deployment_key))
            
        yaml_configs_dict = json.loads(yaml_configs_str) 
        
        return yaml_configs_dict
