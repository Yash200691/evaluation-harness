from pydantic import BaseModel, Field,model_validator
from typing import Any
from run_result import RunResult

class EvaluationResult(BaseModel):
    evaluation_id:str
    task_id:str
    runs:list[RunResult]
    total_runs:int=Field(gt=0)
    successful_runs:int=Field(ge=0)
    pass_rate:float=Field(ge=0, le=1)

@model_validator(mode="after")
def validate_consistency(self):
    # Check 1: Successful runs cannot exceed total runs
    if self.successful_runs > self.total_runs:
        raise ValueError("successful_runs cannot exceed total_runs")

    # Check 2: Total runs must match the runs list
    if self.total_runs != len(self.runs):
        raise ValueError("total_runs must match the length of runs")

    # Check 3: Successful count must match actual results
    actual_successes = sum(1 for run in self.runs if run.success)

    if self.successful_runs != actual_successes:
        raise ValueError(
            "successful_runs must match the number of successful runs"
        )

    # Check 4: Pass rate must match the calculated rate
    expected_rate = (
        self.successful_runs / self.total_runs
        if self.total_runs > 0
        else 0.0
    )

    if abs(self.pass_rate - expected_rate) > 1e-9:
        raise ValueError("pass_rate does not match the calculated success rate")

    return self