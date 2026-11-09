from pydantic import BaseModel,Field
from typing import Any
class Task(BaseModel):
    """
    Represents a task in the agent evaluation framework.

    Attributes:
        task_id (str): The unique identifier for the task.
        description (str): A brief description of the task.
        constraints (dict): The expected format of the input for the task.
        expected_outcome (dict): The expected format of the output for the task.
        max_steps (int): The maximum number of steps allowed to complete the task.
    """

    task_id:str
    description:str
    constraints:dict[str,Any]
    expected_outcome:dict[str,Any]
    max_steps:int =Field(gt=0)