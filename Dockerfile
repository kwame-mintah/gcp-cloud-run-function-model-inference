ARG BUILD_PLATFORM=linux/amd64
ARG BASE_IMAGE=python:3.12.0-slim-bullseye
FROM --platform=${BUILD_PLATFORM} ${BASE_IMAGE}

# Set working directory as `/code/`
WORKDIR /code

# Copy python modules used within application
COPY ./requirements.txt /code/requirements.txt

# Install all python modules, keep image as small as possible
# don't store the cache directory during install
RUN pip install --no-build-isolation --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code to `/code/app/`
COPY . /code

# Copy the service account credentials with role `roles/storage.objectViewer`
# TODO: SecretsUsedInArgOrEnv: Do not use ARG or ENV instructions for sensitive data
ARG PREDICTION_SERVICE_ACCOUNT_CREDENTIALS
ENV GOOGLE_APPLICATION_CREDENTIALS="/code/${PREDICTION_SERVICE_ACCOUNT_CREDENTIALS}"

# Don't run application as root, instead user called `nobody`
RUN chown -R nobody /code

USER nobody

# Start fastapi application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
