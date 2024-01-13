import os
import yaml
from aws_cdk import (
    Stack,
    aws_glue as glue
)
from constructs import Construct
from .stack_configuration import DelloDatalakeGlueWorkflowsStackConfiguration


class DelloDatalakeGlueWorkflowsStack(Stack):

    def __init__(self, 
            scope: Construct, 
            construct_id: str, 
            stack_configuration: DelloDatalakeGlueWorkflowsStackConfiguration = DelloDatalakeGlueWorkflowsStackConfiguration(), 
            **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # WORKFLOWS
        workflows_path = f'{os.getcwd()}/aws_data_engineering/glue/workflows/configs/'
        for workflow_config_file in os.listdir(workflows_path):
            
            with open(workflows_path + workflow_config_file, 'r') as yaml_file:
                glue_jobs_configs = stack_configuration._attribute_variables(yaml.safe_load(yaml_file))
                
            for workflow_name, triggers_config in glue_jobs_configs.items():
                
                glue.CfnWorkflow(self, workflow_name,
                    name = workflow_name,
                    description = triggers_config.pop('description', None)
                )

                for trigger_name, trigger_config in triggers_config.items():
                    glue.CfnTrigger(self, trigger_config.get('id'),
                        name = trigger_name,
                        type = trigger_config.get('type'),
                        schedule = trigger_config.get('schedule'),
                        workflow_name = workflow_name,
                        predicate = glue.CfnTrigger.PredicateProperty(
                            conditions = [
                                glue.CfnTrigger.ConditionProperty(
                                    job_name = job_name,
                                    logical_operator = 'EQUALS',
                                    state = 'SUCCEEDED'
                                )
                                for job_name in trigger_config.get('dependencies', [])
                            ],
                            logical = 'AND'
                        ),
                        actions = [
                            glue.CfnTrigger.ActionProperty(
                                job_name = job_name
                            )
                            for job_name in trigger_config.get('initiates')
                        ]
                    )
        
        
        
        # job = glue.CfnJob(self, 'JobTest1',
        #     name = 'test1', 
        #     role='dello-datalake-dev-glue-jobs-role',
        #     command = glue.CfnJob.JobCommandProperty(
        #         python_version = '3',
        #         name = 'glueetl',
        #         script_location= 's3://location'
        #     )
        # )
        # 
        # job2 = glue.CfnJob(self, 'JobTest2',
        #     name = 'test2', 
        #     role='dello-datalake-dev-glue-jobs-role',
        #     command = glue.CfnJob.JobCommandProperty(
        #         python_version = '3',
        #         name = 'glueetl',
        #         script_location= 's3://location'
        #     )
        # )
        # 
        # glue.CfnJob(self, 'JobTest3',
        #     name = 'test3', 
        #     role='dello-datalake-dev-glue-jobs-role',
        #     command = glue.CfnJob.JobCommandProperty(
        #         python_version = '3',
        #         name = 'glueetl',
        #         script_location= 's3://location'
        #     )
        # )
        # 
        # glue.CfnWorkflow(self, 'WorkfowTest',
        #     name='WorkfowTest'
        # )
        # 
        # 
        # glue.CfnTrigger(self, 'TriggerStart',
        #     name='trigger_start',
        #     type='ON_DEMAND',
        #     workflow_name = 'WorkfowTest',
        #     actions=[
        #         glue.CfnTrigger.ActionProperty(
        #             job_name='test1'
        #         ),
        #         glue.CfnTrigger.ActionProperty(
        #             job_name='test2'
        #         )
        #     ]
        # )
        # 
        # glue.CfnTrigger(self, 'Trigger2',
        #     name='trigger2',
        #     workflow_name = 'WorkfowTest',
        #     type='CONDITIONAL',
        #     actions=[
        #         glue.CfnTrigger.ActionProperty(
        #             job_name='test3'
        #         )
        #     ],
        #     predicate=glue.CfnTrigger.PredicateProperty(
        #         conditions=[
        #             glue.CfnTrigger.ConditionProperty(
        #                 job_name='test1',
        #                 logical_operator='EQUALS',
        #                 state='SUCCEEDED'
        #             ),
        #             glue.CfnTrigger.ConditionProperty(
        #                 job_name='test2',
        #                 logical_operator='EQUALS',
        #                 state='SUCCEEDED'
        #             )
        #         ],
        #         logical="AND"
        #     )
        # )
