import io
import hashlib
import os
import pickle
import traceback
from typing import Tuple

import flask
import pandas as pd
import requests
from sklearn import base

MODEL_SERVER_URL = os.environ["MODEL_SERVER_URL"]


def get_latest_model_hash() -> str:
    """
    Get the hash of the current model from the model server.

    Returns:
        The hash value made available by the model server.
    """
    return requests.get(f"{MODEL_SERVER_URL}/getModelHash").text


def get_current_model_blob() -> bytes:
    """
    Get the hash of the current model from the model server.

    Returns:
        Binary representation of model blob from model server.
    """
    return requests.get(f"{MODEL_SERVER_URL}/getModel").content


def load_model_from_blob(model_blob: bytes) -> base.BaseEstimator:
    """
    Deserialize model blob using pickle.

    Args:
        model_blob: binary-encoded model for deserialization

    Returns:
        Deserialized model
    """
    return pickle.load(io.BytesIO(model_blob))


def update_model(model: base.BaseEstimator,
                 model_hash: str
                 ) -> Tuple[base.BaseEstimator, str]:
    """
    Ensure model is up to date, get new versions if changed.

    Args:
        model: currently-loaded model (deserialized)
        model_hash: latest hash of currently-loaded model blob

    Returns:
        (latest deserialized model, latest deserialized model hash)
    """
    latest_model_hash = get_latest_model_hash()

    if model_hash != latest_model_hash:
        new_model_blob = get_current_model_blob()

        if hashlib.sha1(new_model_blob).hexdigest() != latest_model_hash:
            # TODO(drocco): implement retry/logging of model update failures
            return model, model_hash
        return load_model_from_blob(new_model_blob), latest_model_hash
    return model, model_hash


app = flask.Flask(__name__)
model, model_hash = update_model(bytes(), '')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global model, model_hash
    data = flask.request.get_json()
    input_df = pd.DataFrame.from_dict(data)

    model, model_hash = update_model(model, model_hash)

    prediction = model.predict_proba(input_df)
    output = prediction[0]
    return flask.jsonify(list(output))


@app.route('/getModelHash', methods=['GET'])
def get_model_hash():
    try:
        response = requests.get(f"{MODEL_SERVER_URL}/getModelHash").text
        return f"External hash: {response.text}"
    except Exception:
        return traceback.format_exc()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
