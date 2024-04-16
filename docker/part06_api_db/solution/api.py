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
db_host = os.environ.get("DB_HOST", "localhost")
db_port = os.environ.get("DB_PORT", 5432)
db_user = os.environ.get("DB_USER", "user")
db_password = os.environ.get("DB_PASSWORD", "12345678")
db_name = os.environ.get("DB_NAME", "aihpi")

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

@model_api.get("/feedback", response_model=List[Feedback])
async def get_feedback(conn=Depends(get_db_connection)) -> List[Feedback]:
    query = '''
    SELECT text, language, correct FROM feedback
    '''
    try:
        rows = await conn.fetch(query)
        feedback_list = [Feedback(**row) for row in rows]
        return feedback_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await conn.close()

@model_api.post("/feedback")
async def submit_feedback(feedback: Feedback, conn=Depends(get_db_connection)):
    query = '''
    INSERT INTO feedback(text, language, correct) VALUES($1, $2, $3)
    ON CONFLICT (text, language) DO UPDATE SET correct = EXCLUDED.correct
    '''
    try:
        await conn.execute(query, feedback.text, feedback.language, feedback.correct)
        return {"message": "Feedback created or updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        await conn.close()


model_api.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(model_api, host="0.0.0.0")
