from aws_data_engineering import DelloDatalakeCommonStackConfiguration

class DelloDatalakeGlueWorkflowsStackConfiguration(DelloDatalakeCommonStackConfiguration):
    
    def __init__(self,
            **kwargs) -> None:
        super().__init__(**kwargs)
            