# Machine Learning Engineer Candidate Project

---

## Design

* Factored into two services to allow API to remain active during update:
    * Internal model service – versions and serves latest serialized model
    * External API – serves up predictions via POST request

* Implemented as Docker containers to allow scaling via container orchestration

## Implementation

* Both services are Flask applications

* Using Miniconda as a base Docker image
    * Advantage: environment YAML files are easy to read
    * Disadvantage: Conda environment interface is janky, poorly documented

```docker
FROM continuumio/miniconda3:latest

ADD conda_environment.yml .
RUN conda update -n base -c defaults conda && \
    conda env create -f ./conda_environment.yml

ADD predict.py .

# Default port for Flask applications
EXPOSE 5000

CMD ["conda", "run", "-n", "loanApp", "python", "predict.py"]
```



## Predict API Details

* Predict API just makes predictions, does not handle model files
* Model itself is updated (if necessary) on every request
* Output includes model hash, predicted probability, and class label

```python
@app.route('/predict', methods=['POST'])
def predict() -> str:
    """
    Return model predictions as JSON string.
    """
    global model, model_hash
    # TODO(drocco): implement input schema validation here
    data = flask.request.get_json()
    input_df = pd.DataFrame.from_dict(data)

    model, model_hash = update_model(model, model_hash)

    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    output = {"prediction": int(prediction[0]),
              "predict_proba": list(prediction_proba[0]),
              "model_version": model_hash}

    return flask.jsonify(output)
```
## Model Server Details

* Loads serialized model from object store
    * Just a Docker volume for this prototype
    * Should really be something like Amazon S3 or other scaleable object store

* Custom Flask application to handle versioning of model
    * Model version is tracked via SHA hash
    * File "URI" and hash are configured in `docker-compose.yml`
    * Hash is validated internally

* Model server can be restarted with a new model while predict API remains running

## Quirks/Shortcomings

## Model Improvement

## Demo

* Commands to run
* Swap models
* Restart model server




