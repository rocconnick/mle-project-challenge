# Machine Learning Engineer Candidate Project

---

## Design

* Factored into two services to allow API to remain active during update:
    * Internal model service – versions and serves latest serialized model
    * External API – serves up predictions via POST request

* Implemented as Docker containers to allow scaling via container orchestration

### Not included in solution

* Load balancing and proxy - Kubernetes or cloud container service can handle that
* Web interface for users to manually submit requests
* External logging - any number of loging services could be selected and integrated
* More integration/unit testing - I played a bit fast and loose here, there's not a boatload of actual logic

---

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

---

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

---


## Model Server Details

* Loads serialized model from object store
    * Model just stored on a Docker volume for this prototype
    * Should really be something like Amazon S3 or other scaleable object store

* Custom Flask application to handle versioning of model
    * Model version is tracked via SHA hash
    * File "URI" and hash are configured in `docker-compose.yml`
    * Hash is validated internally

* Model server can be restarted with a new model while predict API remains running

---

## Model Improvement

* Extreme class imbalance - late-payment probability never exceeds 50% for test set
    * Accuracy/precision/recall all don't measure anything meaningful
    * ROC-AUC is better, appropriate interpretation: "probability two randomly sampled predictions are ranked correctly"

| Model                   | Train AUC | Test AUC | Comment                               |
|-------------------------|:---------:|:--------:|---------------------------------------|
| Original Random Forest  |    1.0    | 0.62     | Terrible generalization               |
| Optimized Random Forest |    0.85   | 0.74     | Better test score, but still overfit  |
| Gradient Boosted Model  |    0.75   | 0.75     | Best performance, good generalization |

![ROC Curve](img/roc_auc.png "ROC Curve")

