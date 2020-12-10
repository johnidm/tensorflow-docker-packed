import numpy as np
import tensorflow as tf
import pickle
import fastapi
from typing import Dict
import uvicorn

from pydantic import BaseModel
import os

from tensorflow.keras.preprocessing.sequence import pad_sequences

app = fastapi.FastAPI()

ROOT_PATH = os.getcwd()


model = tf.keras.models.load_model(f"{ROOT_PATH}/app/model")

with open(os.path.join(ROOT_PATH, f"{ROOT_PATH}/app/model/model.bin"), "rb") as f:
    (tokenizer,) = pickle.load(f)


class DoIn(BaseModel):
    text: str


class DoOut(BaseModel):
    text: str
    targets: Dict[str, float]


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
    text = do.text

    padded_text = pad_sequences(
        tokenizer.texts_to_sequences([text]), maxlen=250, truncating="post"
    )

    predict = model.predict(padded_text)

    targets = {}
    for index, ele in enumerate(predict[0]):
        targets[str(index)] = str(round(ele, 2))

    return {
        "text": text,
        "targets": targets,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")