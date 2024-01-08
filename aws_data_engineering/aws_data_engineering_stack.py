from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3
)
import os
from constructs import Construct
from stack_configuration import CloudFormationStackConfiguration

class AwsDataEngineeringStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        stack_configuration = CloudFormationStackConfiguration()
        
   
        self.raw_bucket=s3.Bucket(self, "AwsDataEngineeringRawBucket",
            bucket_name=f"dellotech-{stack_configuration.environment}-raw-{stack_configuration.aws_account_id}-{stack_configuration.aws_region}",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True
        )
        
        self.trusted_bucket=s3.Bucket(self, "AwsDataEngineeringTrustedBucket",
            bucket_name=f"dellotech-{stack_configuration.environment}-trusted-{stack_configuration.aws_account_id}-{stack_configuration.aws_region}",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True
        )
        
        self.refined_bucket=s3.Bucket(self, "AwsDataEngineeringRefinedBucket",
            bucket_name=f"dellotech-{stack_configuration.environment}-refined-{stack_configuration.aws_account_id}-{stack_configuration.aws_region}",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True
        )
        
        
