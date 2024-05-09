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
                glue_workflows_configs = stack_configuration._attribute_variables(yaml.safe_load(yaml_file))
                
            for workflow_name, triggers_config in glue_workflows_configs.items():
                
                glue.CfnWorkflow(self, triggers_config.pop('id'),
                    name = workflow_name,
                    description = triggers_config.pop('description', None),
                    max_concurrent_runs = triggers_config.pop('max_concurrent_runs', None),
                    tags = triggers_config.pop('tags', None)
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
                                for job_name in trigger_config.get('dependencies')
                            ],
                            logical = 'AND'
                        ) if trigger_config.get('dependencies') else None,
                        actions = [
                            glue.CfnTrigger.ActionProperty(
                                job_name = job_name
                            )
                            for job_name in trigger_config.pop('initiates')
                        ],
                        tags = trigger_config.get('tags')
                    )
