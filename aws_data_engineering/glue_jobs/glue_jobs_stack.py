from aws_cdk import (
    Stack,
    aws_glue as glue,
    aws_iam as iam
)
import os
from constructs import Construct
from .stack_configuration import DelloDatalakeGlueJobsStackConfiguration

class DellotechGlueJobsDatalakeStack(Stack):

    def __init__(self, 
            scope: Construct, 
            construct_id: str, 
            stack_configuration: DelloDatalakeGlueJobsStackConfiguration = DelloDatalakeGlueJobsStackConfiguration(), 
            **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
                
        # GLUE JOBS ROLE
        self.glue_jobs_role = iam.Role(self, 'dello-datalake-glue-jobs-role',
            role_name = stack_configuration.glue_jobs_role_name,                           
            assumed_by = iam.ServicePrincipal('glue.amazonaws.com'),
            description = 'Role to be attached to Glue Jobs to read data from s3'
        )

        # RAW-TO-TRUSTED
        self.raw_to_trusted_job = glue.CfnJob(self, 'dello-datalake-glue-job-raw-to-trusted',
            name = stack_configuration.raw_to_trusted_job_name,
            description = 'Job resposible for process data from Raw Zone and send it to Trusted Zone',
            max_retries = 3,
            glue_version = 'V3_0',
            command = glue.CfnJob.JobCommandProperty(
                python_version = '3.9.6',
                script_location = os.path.join(os.getcwd(), 'scripts/raw-to-trusted.py')
            ),
            tags = stack_configuration.jobs_tags,
            role = stack_configuration.glue_jobs_role_name
        )
        
        # TRUSTED-TO-REFINED
        self.raw_to_trusted_job = glue.CfnJob(self, 'dello-datalake-glue-job-trusted-to-refined',
            name = stack_configuration.trusted_to_refined_job_name,
            description = 'Job resposible for process data from Trusted Zone and send it to Refined Zone',
            max_retries = 3,
            glue_version = 'V3_0',
            command = glue.CfnJob.JobCommandProperty(
                python_version = '3.9.6',
                script_location = os.path.join(os.getcwd(), 'scripts/trusted-to-refined.py')
            ),
            tags = stack_configuration.jobs_tags,
            role = stack_configuration.glue_jobs_role_name
        )
        
        # GLUE JOBS POLICY           
        self.glue_jobs_role.add_to_policy(iam.PolicyStatement(
            effect = iam.Effect.ALLOW,
            resources = [
                f"arn:aws:glue:{stack_configuration.aws_region}:{stack_configuration.aws_account_id}:job/{stack_configuration.raw_to_trusted_job_name}",
                f"arn:aws:glue:{stack_configuration.aws_region}:{stack_configuration.aws_account_id}:job/{stack_configuration.trusted_to_refined_job_name}"
            ],
            actions = ['s3:ListBucket', 's3:PutObject', 's3:DeleteObject']
        ))
        
        
        
        
