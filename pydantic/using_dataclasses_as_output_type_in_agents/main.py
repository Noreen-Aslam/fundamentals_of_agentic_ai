from pydantic.dataclasses import dataclass

# Define structured output for an AI agent
@dataclass
class TaskResult:
    task: str
    status: str
    time_taken: int

# Example: agent output simulation
result = TaskResult(task="Data Cleaning", status="Completed", time_taken=5)

print(result)
# TaskResult(task='Data Cleaning', status='Completed', time_taken=5)
