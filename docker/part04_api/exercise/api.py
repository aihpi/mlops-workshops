from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn
import joblib
from typing import Tuple
import sklearn
import numpy as np
import os

root_path = os.environ.get("ROOT_PATH", "")
model_api = FastAPI(root_path=root_path)

class Result(BaseModel):
    language : str

def get_model() -> Tuple[sklearn.base.BaseEstimator, np.matrix]:
    full_model = joblib.load("models/multinomial_language_detector.joblib")
    return full_model

# TODO: implement predict endpoint


model_api.mount("/", StaticFiles(directory="static", html=True), name="static")
if __name__ == "__main__":
    uvicorn.run(model_api, host="0.0.0.0")
