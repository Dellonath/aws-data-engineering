from aws_cdk import (
    Stack,
    aws_glue as glue,
    aws_iam as iam
)
import os
from constructs import Construct
from .stack_configuration import DelloDatalakeGlueJobsStackConfiguration
import json
import yaml

class DellotechGlueJobsDatalakeStack(Stack):

    def __init__(self, 
            scope: Construct, 
            construct_id: str, 
            stack_configuration: DelloDatalakeGlueJobsStackConfiguration = DelloDatalakeGlueJobsStackConfiguration(), 
            **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
                
        # GLUE JOBS ROLE
        self.glue_jobs_role = iam.Role(self, 'DelloDatalakeGlueJobsRole',
            role_name = stack_configuration.glue_jobs_role_name,                           
            assumed_by = iam.ServicePrincipal('glue.amazonaws.com'),
            description = 'Role to be attached to Glue Jobs to read data from s3'
        )
        
        self.glue_jobs_role.add_to_policy(iam.PolicyStatement(
            effect = iam.Effect.ALLOW,
            resources = [
                f"arn:aws:s3:::{stack_configuration.raw_bucket_name}",
                f"arn:aws:s3:::{stack_configuration.trusted_bucket_name}",
                f"arn:aws:s3:::{stack_configuration.refined_bucket_name}"
            ],
            actions = ['s3:getObject', 's3:ListBucket', 's3:PutObject', 's3:DeleteObject']
        ))
        
        with open(f'{os.getcwd()}/aws_data_engineering/glue_jobs/configs/glue_jobs.yml', 'r') as file:
            glue_jobs_configs = self.__attribute_variables_to_yaml_config(yaml.safe_load(file))

        # RAW-TO-TRUSTED
        for glue_job_config in glue_jobs_configs.keys():
            
            glue.CfnJob(self, 
                name = glue_job_config,
                command = glue.CfnJob.JobCommandProperty(
                    name = 'glueetl',
                    python_version = '3',
                    script_location = os.path.join(os.getcwd(), glue_jobs_configs[glue_job_config].pop('script_location'))
                ),
            **glue_jobs_configs[glue_job_config])
        
        # TRUSTED-TO-REFINED
        # self.raw_to_trusted_job = glue.CfnJob(self, 'DelloDatalakeGlueJobTrustedToRefined',
        #     name = stack_configuration.trusted_to_refined_job_name,
        #     description = 'Job resposible for process data from Trusted Zone and send it to Refined Zone',
        #     max_retries = 3,
        #     glue_version = '3.0',
        #     command = glue.CfnJob.JobCommandProperty(
        #         name = 'glueetl',
        #         python_version = '3',
        #         script_location = os.path.join(os.getcwd(), 'scripts/trusted-to-refined.py')
        #     ),
        #     tags = stack_configuration.jobs_tags,
        #     role = stack_configuration.glue_jobs_role_name
        # )
        
    def __attribute_variables_to_yaml_config(self, config: dict) -> dict:
        
        environment='dev'
    
        yaml_configs_str = f'{json.dumps(config)}'.replace('{environment}', environment)
        yaml_configs_dict = json.loads(yaml_configs_str) 
        return yaml_configs_dict
        
        
        
        
        
