from fastapi import FastAPI, Form, Depends, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn
import joblib
from typing import Tuple, List
import sklearn
import numpy as np
import os
import asyncpg

root_path = os.environ.get("ROOT_PATH", "")
# TODO: get env vars for DB


model_api = FastAPI(root_path=root_path)

class Result(BaseModel):
    language: str

class Feedback(BaseModel):
    text: str
    language: str
    correct: bool

async def get_db_connection():
    return await asyncpg.connect(
        user=db_user, password=db_password, database=db_name,
        host=db_host, port=db_port)

def get_model() -> Tuple[sklearn.base.BaseEstimator, np.matrix]:
    full_model = joblib.load("models/multinomial_language_detector.joblib")
    return full_model

@model_api.post("/predict", response_model=Result)
async def predict(input_text: str = Form(), full_model: Tuple = Depends(get_model)) -> Result:
    model, cv = full_model
    vectorized = cv.transform([input_text])
    language_prediction = model.predict(vectorized)[0]
    return Result(language=language_prediction)

# TODO: implement GET and POST method for /feedback



model_api.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(model_api, host="0.0.0.0")
