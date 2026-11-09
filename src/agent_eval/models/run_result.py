from pydantic import BaseModel, Field
from typing import Any
from trajectory import TrajectoryStep

class RunResult(BaseModel):
    """
    Represents the result of a run in the agent evaluation framework.

    Attributes:
        run_id (str): The unique identifier for the run.
        task_id (str): The unique identifier for the task associated with the run.
        success (bool): Indicates whether the run was successful or not.
        trajectory (list[TrajectoryStep]): The trajectory of the run.
        total_latency_ms (float): The total latency of the run in milliseconds.
        total_cost_usd (float): The total cost of the run in USD.
        failure_reason (str | None): An optional reason for the failure if the run failed.
    """

    run_id: str
    task_id: str
    trajectory:list[TrajectoryStep]
    success: bool
    total_latency_ms:float=Field(gt=0)
    total_cost_usd:float=Field(gt=0)
    failure_reason:str|None=None
    