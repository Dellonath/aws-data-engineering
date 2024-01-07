import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_data_engineering.aws_data_engineering_stack import AwsDataEngineeringStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_data_engineering/aws_data_engineering_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsDataEngineeringStack(app, "aws-data-engineering")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
