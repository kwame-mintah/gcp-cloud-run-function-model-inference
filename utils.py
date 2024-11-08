import logging
from typing import Any

import dill
from google.cloud import storage
from pydantic import Field
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    GCP_MLFLOW_MODEL_ARTIFACT_BUCKET_NAME: str = Field(
        description="The GCP bucket name, where the model artifact has been uploaded"
    )
    USE_LOCAL_FILE_PATH_MODEL: bool = Field(
        default=False,
        description="Use the model artifact found locally, rather than fetching from GCP bucket.",
    )


def load_object(file_path: str) -> Any:
    """
    Load file into python and return serialized object.

    :param file_path: file location
    :return: object
    """
    try:
        with open(file_path, "rb") as f:
            obj = dill.load(file=f)
        return obj
    except Exception as e:
        logging.info(f"Error in load_object: {str(e)}")
        raise e


def download_blob_and_return_object(
    bucket_name: str = EnvironmentVariables().GCP_MLFLOW_MODEL_ARTIFACT_BUCKET_NAME,
    source_blob_name: str = "model.pkl",
    destination_file_name: str = "gcp_model.pkl",
) -> Any:
    """
    Downloads a blob from the bucket and return serialized object

    :param destination_file_name:
    :param bucket_name: The ID of your GCS bucket
    :param source_blob_name: The ID of your GCS object
    :return: serialized object
    """

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    return load_object(destination_file_name)
