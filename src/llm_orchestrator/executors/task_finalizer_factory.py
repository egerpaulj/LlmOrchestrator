from llm_orchestrator.core.task import WorkflowTask
from llm_orchestrator.data_store.repository import WorkflowRepository
from llm_orchestrator.executors.task_finalizer import DefaultStepFinalizer, StepFinalizer

class TaskFinalizerFactory:
    workflow_repository : WorkflowRepository

    def create_task_finalizer(self, task: WorkflowTask) -> StepFinalizer:
        if task.result_model_name == "FAIL":
            raise ValueError("Failed")
        
        return DefaultStepFinalizer(workflow_repository=self.workflow_repository)