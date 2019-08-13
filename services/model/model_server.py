import os
import hashlib

import flask


def check_hash(model_blob: bytes, model_sha: str) -> None:
    """
    Raise descriptive error if SHA1 hash differs from expected.

    Args:
        model_blob: bytes object read from model pickle
        model_sha: expected SHA1 hash

    Raises:
        ValueError: if hash does not match
    """
    model_blob_hash = hashlib.sha1(model_blob).hexdigest()
    if model_blob_hash != model_sha:
        raise ValueError(
            f"""
            SHA1 hash for model file does not match MODEL_SHA in environment
            expected: {model_sha}
            found: {model_blob_hash}""")


def main() -> None:
    """
    Run the model server flask application.

    Retrives path to model and SHA checksum from environment, loads model file,
    and defines an API for retrieving the model.
    """

    app = flask.Flask(__name__)

    model_sha = os.environ["MODEL_SHA"]
    model_path = os.path.join(os.environ["MODEL_DIR"],
                              os.environ["MODEL_FILE_NAME"])

    model_blob = open(model_path, 'rb').read()

    check_hash(model_blob, model_sha)

    @app.route('/getModel', methods=['GET'])
    def get_model():
        """
        Return the loaded model blob.
        """
        return model_blob

    @app.route('/getModelHash', methods=['GET'])
    def get_model_hash():
        """
        Return the checksum of the loaded model.
        """
        return model_sha

    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
