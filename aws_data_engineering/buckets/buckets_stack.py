from aws_cdk import (
    Stack,
    aws_s3 as s3
)

from constructs import Construct
from .stack_configuration import DelloDatalakeBucketsStackConfiguration

class DellotechBucketsDatalakeStack(Stack):

    def __init__(self, 
            scope: Construct, 
            construct_id: str, 
            stack_configuration: DelloDatalakeBucketsStackConfiguration = DelloDatalakeBucketsStackConfiguration(), 
            **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # RAW BUCKET
        self.raw_bucket = s3.Bucket(self, 'DelloDatalakeBucketRaw',
            bucket_name = stack_configuration.raw_bucket_name,
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            encryption = s3.BucketEncryption.S3_MANAGED,
            versioned = True
        )
        
        # TRUSTED BUCKET
        self.trusted_bucket = s3.Bucket(self, 'DelloDatalakeBucketTrusted',
            bucket_name = stack_configuration.trusted_bucket_name,
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            encryption = s3.BucketEncryption.S3_MANAGED,
            versioned = True
        )
        
        # REFINED BUCKET
        self.refined_bucket = s3.Bucket(self, 'DelloDatalakeBucketRefined',
            bucket_name = stack_configuration.refined_bucket_name,
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            encryption = s3.BucketEncryption.S3_MANAGED,
            versioned = True
        )
        
        # UTILITIES
        self.utilities_bucket = s3.Bucket(self, 'DelloDatalakeBucketUtilities',
            bucket_name = stack_configuration.utilities_bucket_name,
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            encryption = s3.BucketEncryption.S3_MANAGED,
            object_ownership = s3.ObjectOwnership.BUCKET_OWNER_PREFERRED,
            versioned = True
        )
        
        
