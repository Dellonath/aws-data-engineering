import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_data_engineering.s3.buckets_stack import DelloDatalakeS3BucketsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_data_engineering/aws_data_engineering_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DelloDatalakeS3BucketsStack(app, 'aws_data_engineering')
    template = assertions.Template.from_stack(stack)
    
    # 1. test utility bucket name using regex
    # 2. test utility bucket permissions to accept ACLs to upload glue job scripts 

#     template.has_resource_properties('AWS::SQS::Queue', {
#         'VisibilityTimeout': 300
#     })
