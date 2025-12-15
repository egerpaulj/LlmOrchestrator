from typing import Type
from pydantic import BaseModel
from llm_orchestrator.core.workflow import Workflow
from llm_orchestrator.inference_api.llm_config import LlmConfig
from llm_orchestrator.inference_api.strategies.base import LLMProviderStrategy
from llm_orchestrator.inference_api.strategies.strategy_factory import create_inference_strategy_local

class WorkflowExecutor:
    
    llm_config: LlmConfig
    
    def get_model_class(self, type_name: str) -> Type[BaseModel]:
        model_class = globals().get(type_name, None)
        if model_class is None:
            raise ValueError(f"Model class '{type_name}' not found in global namespace")
        return model_class

    def execute_workflow(self, workflow: Workflow):
        for task in workflow.tasks:
            llm_inference = create_inference_strategy_local(name = task.strategy, llm_config=self.llm_config)
            result = llm_inference.inference(
                model=task.model, 
                prompt=task.user_prompt,
                system=task.system_prompt, 
                json_response_type= 
                self.get_model_class(task.result_model_name))
            task.result = result.model_dump_json()
        