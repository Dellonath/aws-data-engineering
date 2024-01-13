import os
import yaml
from aws_cdk import (
    Stack,
    aws_glue as glue,
    aws_iam as iam
)
from constructs import Construct
from .stack_configuration import DelloDatalakeGlueJobsStackConfiguration

class DelloDatalakeGlueJobsStack(Stack):

    def __init__(self, 
            scope: Construct, 
            construct_id: str, 
            stack_configuration: DelloDatalakeGlueJobsStackConfiguration = DelloDatalakeGlueJobsStackConfiguration(), 
            **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        
        self.aws_account_id = stack_configuration.aws_account_id
        self.aws_region = stack_configuration.aws_region
        self.deployment_key = stack_configuration.deployment_key
               
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
            actions = [
                's3:getObject', 
                's3:ListBucket', 
                's3:PutObject', 
                's3:DeleteObject'
            ]
        ))
        
        self.glue_jobs_role.add_to_policy(iam.PolicyStatement(
            effect = iam.Effect.ALLOW,
            resources = [
                f"arn:aws:s3:::{stack_configuration.utilities_bucket_name}"
            ],
            actions = [
                's3:getObject', 
                's3:ListBucket'
            ]
        ))
        
        # GLUE JOBS
        jobs_path = f'{os.getcwd()}/aws_data_engineering/glue/jobs/configs/'
        for jobs_config_file in os.listdir(jobs_path):
            
            with open(jobs_path + jobs_config_file, 'r') as yaml_file:
                glue_jobs_configs = stack_configuration._attribute_variables(yaml.safe_load(yaml_file))

            for job_name, job_config in glue_jobs_configs.items():
                
                glue.CfnJob(self, 
                    name = job_name,
                    command = glue.CfnJob.JobCommandProperty(
                        **job_config.pop('command')
                    ),
                    **job_config)  
        