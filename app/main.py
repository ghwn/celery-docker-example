from celery.result import AsyncResult
from fastapi import FastAPI

from app.celery.tasks import add

app = FastAPI()


@app.post("/add")
async def add_numbers(x: int, y: int):
    result = add.delay(x, y)
    return {"task_id": result.id, "status": "Task submitted"}


@app.get("/tasks/{task_id}")
async def get_result(task_id: str):
    result = AsyncResult(task_id)
    if result.ready():
        return {"task_id": task_id, "result": result.result}
    else:
        return {"task_id": task_id, "status": "Task is still processing"}
