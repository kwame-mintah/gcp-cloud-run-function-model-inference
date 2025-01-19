import os

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app=app)


@pytest.fixture(autouse=True)
def set_environment_variables(monkeypatch):
    """Set environment variable needed for application"""
    del os.environ["GCP_MLFLOW_MODEL_ARTIFACT_BUCKET_NAME"]
    os.environ["USE_LOCAL_FILE_PATH_MODEL"] = "True"
    os.environ["GCP_MLFLOW_MODEL_ARTIFACT_BUCKET_NAME"] = "mlflow-bucket"


def test_predict_wine_quality():
    response = client.post(
        url="/predict/",
        json=[
            {
                "alcohol": 12.8,
                "chlorides": 0.029,
                "citric acid": 0.48,
                "density": 0.98,
                "fixed acidity": 6.2,
                "free sulfur dioxide": 29,
                "pH": 3.33,
                "residual sugar": 1.2,
                "sulphates": 0.39,
                "total sulfur dioxide": 75,
                "volatile acidity": 0.66,
            }
        ],
    )

    assert response.status_code == 200
    assert response.json() == [6.507185441498436]
