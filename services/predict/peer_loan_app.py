import os
import pickle

import flask
import pandas as pd


app = flask.Flask(__name__)
model_path = os.path.join(os.environ["MODEL_DIR"],
                          os.environ["MODEL_FILE_NAME"])
model = pickle.load(open(model_path, 'rb'))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = flask.request.get_json()
    input_df = pd.DataFrame.from_dict(data)
    prediction = model.predict_proba(input_df)
    output = prediction[0]
    return flask.jsonify(list(output))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
