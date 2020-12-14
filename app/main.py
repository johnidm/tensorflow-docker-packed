import numpy as np
import tensorflow as tf
import pickle
import fastapi
from typing import Dict
import uvicorn

from pydantic import BaseModel
import os

app = fastapi.FastAPI()

ROOT_PATH = os.getcwd()


model = tf.keras.models.load_model(f"{ROOT_PATH}/app/model")


class DoIn(BaseModel):
    text: str


class DoOut(BaseModel):
    text: str
    label: str
    score: float


class HomeOut(BaseModel):
    status: str
    versions: Dict[str, str]


@app.get("/", response_model=HomeOut)
def get_home():
    return {
        "status": "Running RESTful Machine Learning",
        "versions": {
            "numpy": np.__version__,
            "tensorflow": tf.__version__,
            "fastapi": fastapi.__version__,
        },
    }


@app.post("/do", status_code=fastapi.status.HTTP_201_CREATED, response_model=DoOut)
def do_post(do: DoIn):

    class_names = [
        "ciencia e tecnologia",
        "economia",
        "entretenimento",
        "esportes",
        "politica",
    ]

    text = do.text

    predicts = model.predict([text])

    predicted_scores = tf.keras.backend.flatten(predicts)
    predicted_index = tf.argmax(predicted_scores, axis=0)

    predicted_label = class_names[predicted_index]
    predicted_score = predicted_scores[predicted_index]

    return {
        "text": text,
        "label": predicted_label,
        "score": predicted_score,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")