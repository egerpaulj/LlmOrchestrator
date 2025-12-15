from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    
        
    
class McpTools(BaseModel):
    name: str = Field(description="Name of the MCP tool-set")
    description: str = Field(description="Description of what the tools can do")
    json_str: str = Field(description="The json description of the tools")


class WorkflowTask(BaseModel):
    description: str = Field(description="Description of the task to perform")
    name: str = Field(description="Unique task name")
    priority: int = Field(0,description="Priority of the task; higher numbers indicate higher priority",)
    status: TaskStatus = Field(TaskStatus.PENDING,description="Current status of the task",)
    user_prompt: str = Field(description="User prompt for the model",)
    system_prompt: str = Field(description="System prompt for the model",)
    context: Dict[str, str] = Field(
        default_factory=dict,
        description="Contextual data to provide additional information for the task",
    )
    strategy:str = Field(description="Strategy identifier to select an execution strategy",)
    model: str = Field(description="Model identifier to use for inference",)
    mcp_tools: Optional[McpTools] = Field(None,description="List of MCP tool identifiers used during task execution",)
    result: Optional[str] = Field(None, description="Result produced by the task")
    result_model_name: str = Field(description="The type name of the result. Must be pydantic")
    

