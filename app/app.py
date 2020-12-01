from flask import Flask, request, jsonify

import numpy as np
import tensorflow as tf
import flask
import pickle

import os

from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

ROOT_PATH = os.getcwd()


model = tf.keras.models.load_model(f"{ROOT_PATH}/app/model")

with open(os.path.join(ROOT_PATH, f"{ROOT_PATH}/app/model/model.bin"), "rb") as f:
    (tokenizer,) = pickle.load(f)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "status": "Running RESTful Machine Learning",
            "versions": {
                "numpy": np.__version__,
                "tensorflow": tf.__version__,
                "flask": flask.__version__,
            },
        }
    )


@app.route("/do", methods=["POST"])
def do():
    content = request.json
    text = content.get("text", "")

    padded_text = pad_sequences(
        tokenizer.texts_to_sequences([text]), maxlen=250, truncating="post"
    )

    predict = model.predict(padded_text)

    targets = {}
    for index, ele in enumerate(predict[0]):
        targets[str(index)] = str(round(ele, 2))

    app.logger.info(targets)

    return (
        jsonify(
            {
                "text": text,
                "targets": targets,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
