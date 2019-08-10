import os
import hashlib
from typing import Any

import flask


def get_sha1_hash(obj: Any) -> str:
    """
    Get the SHA1 hash of an object.

    Args:
        obj: python object to take hash

    Returns:
        Hex digest of SHA1 has for object
    """
    h = hashlib.sha1()
    h.update(obj)
    return h.hexdigest()


def check_hash(model_blob: bytes) -> None:
    """
    Check validity of loaded model blob against expected hash.

    Args:
        model_blob: bytes object read from model pickle

    Raises:
        ValueError: if hash does not match
    """
    if get_sha1_hash(model_blob) != model_sha:
        raise ValueError(
            f"""SHA1 hash for file does not match MODEL_SHA in environment"
                MODEL_DIR: {os.environ['MODEL_DIR']}
                MODEL_FILE_NAME: {os.environ['MODEL_FILE_NAME']}
                MODEL_SHA: {os.environ['MODEL_SHA']}""")


app = flask.Flask(__name__)
model_sha = os.environ["MODEL_SHA"]
model_path = os.path.join(os.environ["MODEL_DIR"],
                          os.environ["MODEL_FILE_NAME"])
model_blob = open(model_path, 'rb').read()
check_hash(model_blob)


@app.route('/getModel', methods=['GET'])
def get_model():
    return model_blob


@app.route('/getModelHash', methods=['GET'])
def get_model_hash():
    return model_sha


if __name__ == '__main__':
    app.run(host='0.0.0.0')
