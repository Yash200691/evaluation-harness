from pydantic import BaseModel
from typing import Any
class ToolCall(BaseModel):
    """
    Represents a tool call in the agent evaluation framework.

    Attributes:
        tool_name (str): The name of the tool being called.
        arguments (dict): A dictionary of arguments to be passed to the tool.
        call_id (str): A unique identifier for the tool call.
    """

    tool_name: str
    arguments: dict[str, Any]
    call_id: str