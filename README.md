# Google Platform Cloud (GCP) Function Model Inference

A cloud function to invoke a prediction against a machine learning model that has been trained outside
of a cloud provider, using tools like [MLFlow](https://mlflow.org/). This repository will not contain
the model artifact output, but the code for the cloud function.

FastAPI will be used for the cloud function as it offers many features e.g. authentication, body validation etc.
and overall easy to use and maintain.

# Architecture

![proposed-model-inference-architecture](./docs/drawio/cloud-function-model-inference-overview.png)

1. External to GCP model training is performed and model artifact output,
2. User makes a request to a HTTP endpoint for a prediction,
3. Model artifact is stored within a bucket, when function is invoked -- model is downloaded,
4. Prediction is output via a HTTP response.

# Training using MLflow

As with all machine learning projects, your milage may vary (YMMV). This project will re-use existing data set for
modeling wine preferences using [mlflow-example](https://github.com/mlflow/mlflow-example) for demonstration. The provided
`docker-compose.yml` file will create the necessary resources needed to train locally. The following steps below will
start the services:

1. Start mflow server, postgres and minio:

```shell
docker compose up -d --build
```

2. Access MLflow UI with http://localhost:5001
3. Access MinIO UI with http://localhost:9000, login with credentials passed used in the `docker-compose.yml`

> [!NOTE]
>
> Because the MLflow is a custom docker image, passing `--build` arg will cause the docker image to be re-built each time
> which is helpful when amending the `.mlflow/requirements.txt`. A re-build is not needed each time, if there is no changes
> being made to the file and `---build` can be omitted from the command.

# References

1. [How to serve deep learning models using TensorFlow 2.0 with Cloud Functions](https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions) by Rustem Feyzkhanov
