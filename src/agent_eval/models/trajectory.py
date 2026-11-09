from pydantic import BaseModel, Field
from typing import Any
from tool_call import ToolCall
from datetime import datetime

class TrajectoryStep(BaseModel):

    step_number: int=Field(gt=0)
    tool_call: ToolCall
    tool_result:Any
    success: bool
    error:str|None = None
    timestamp: datetime
    latency_ms: float=Field(gt=0)


obj1=TrajectoryStep(
    step_number=1,
    tool_call=ToolCall(
        tool_name="sample_tool",
        arguments={"arg1": "value1", "arg2": 2},
        call_id="call_001"
    ),
    tool_result={"result": "success"},
    success=True,
    error=None,
    timestamp=datetime.now(),
    latency_ms=150.5
)

print(obj1)