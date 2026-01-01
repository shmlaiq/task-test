from fastapi import FastAPI

app = FastAPI()

@app.get("/tasks")
def todo() -> list[dict[str, int | str]]:
    return [{"id": 1, "task": "Task 1 completed"}, 
            {"id": 2, "task": "Task 2 completed"}]

@app.get("/tasks/{task_id}")
async def todo_one(task_id: int =1, include_details: bool = False) -> dict[str, int | str]:
    if task_id < 1:
        return {"error": "Invalid task ID must be greater than 0"}
    if include_details:
        return {"id": task_id, "task": "include_details must be a boolean value TRUE", "details": "Detailed information about the task TRUE"}
    return {"id": task_id, "task": "Task retrieved successfully with FALSE details"}
