#!/usr/bin/env python3

import aws_cdk as cdk

from aws_data_engineering.buckets.buckets_stack import DellotechBucketsDatalakeStack
from aws_data_engineering.glue_jobs.glue_jobs_stack import DellotechGlueJobsDatalakeStack

app = cdk.App()
DellotechBucketsDatalakeStack(app, 'DellotechBucketsDatalakeStack')
DellotechGlueJobsDatalakeStack(app, 'DellotechGlueJobsDatalakeStack')

app.synth()
