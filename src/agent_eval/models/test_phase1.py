from task import Task
from tool_call import ToolCall

obj1=Task(
    task_id="task_001",
    description="This is a sample task.",
    constraints={"input_format": "string"},
    expected_outcome={"output_format": "string"},
    max_steps=5
)
obj2=ToolCall(
    tool_name="sample_tool",
    arguments={"arg1": "value1", "arg2": 2},
    call_id="call_001"
)

print(obj1)
print(obj2)