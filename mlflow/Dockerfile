ARG MINICONDA_OS_ARCHITECTURE=x86_64
ARG MINICONDA_PYTHON_VERSION=py312_24.9.2-0
ARG BUILD_PLATFORM=linux/amd64
# Might run into issues when building docker image on Apple Silicon
# have set the platform to linux/amd64 to resolve the issue when installing
# miniconda an error is thrown.
FROM --platform=${BUILD_PLATFORM} python:3.12.0-slim-bullseye
# Copy requirements.txt
COPY requirements.txt /tmp
# Install git CLI for running Mlflow from Git repositories and python packages
# Also install conda needed for mlflow environment
# https://repo.anaconda.com/archive/ OR https://repo.anaconda.com/miniconda/
ARG MINICONDA_PYTHON_VERSION
ARG MINICONDA_OS_ARCHITECTURE
RUN pip install -r /tmp/requirements.txt \
    && apt-get update \
    && apt-get install wget git  -y \
    && apt-get clean \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_PYTHON_VERSION}-Linux-${MINICONDA_OS_ARCHITECTURE}.sh -O ~/miniconda.sh \
    && bash ~/miniconda.sh -p /miniconda -b \
    && rm ~/miniconda.sh
ENV PATH=/miniconda/bin:${PATH}
# Resolve issue related to /lib/x86_64-linux-gnu/libstdc++.so.6: version 'GLIBCXX_3.4.29' not found
# Solution as per: https://github.com/pybind/pybind11/discussions/3453#discussioncomment-7068951
RUN conda install -y -c conda-forge libstdcxx-ng \
    && rm /usr/lib/${MINICONDA_OS_ARCHITECTURE}-linux-gnu/libstdc++.so.6 \
    && cp miniconda/lib/libstdc++.so.6 /usr/lib/${MINICONDA_OS_ARCHITECTURE}-linux-gnu/
