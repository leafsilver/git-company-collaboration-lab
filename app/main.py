from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task Summary API")

TASKS = {
    1: {
        "id": 1,
        "title": "Prepare release notes",
        "status": "in_progress",
    },
    2: {
        "id": 2,
        "title": "Deploy application",
        "status": "pending",
    },
}


@app.get("/tasks/{task_id}/summary")
def get_task_summary(task_id: int) -> dict[str, object]:
    task = TASKS.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        **task,
        "summary": f"{task['title']} [{task['status']}]",
    }
