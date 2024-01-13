#!/usr/bin/env python3

import aws_cdk as cdk
from aws_data_engineering.s3.buckets_stack import DelloDatalakeS3BucketsStack
from aws_data_engineering.glue.jobs.glue_jobs_stack import DelloDatalakeGlueJobsStack
from aws_data_engineering.glue.workflows.glue_workflows_stack import DelloDatalakeGlueWorkflowsStack

app = cdk.App()
DelloDatalakeS3BucketsStack(app, 'DelloDatalakeS3BucketsStack')
DelloDatalakeGlueJobsStack(app, 'DelloDatalakeGlueJobsStack')
DelloDatalakeGlueWorkflowsStack(app, 'DelloDatalakeGlueWorkflowsStack')

app.synth()
