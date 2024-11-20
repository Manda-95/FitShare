from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class TrainingPlan(BaseModel):
    id: int
    title: str
    level: str
    goal: str


@app.get("/plans", response_model=List[TrainingPlan])
def get_plans(level: str = None, goal: str = None, sport: str = None):
    filtered = training_plans
    if level:
        filtered = [plan for plan in filtered if plan["level"] == level]
    if goal:
        filtered = [plan for plan in filtered if plan["goal"] == goal]
    if sport:
        filtered = [plan for plan in filtered if plan["sport"] == sport]
    return filtered    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}