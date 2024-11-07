# Might run into issues when building docker image on Apple Silicon
# have set the platform to linux/amd64 to resolve the issue when installing
# miniconda an error is thrown.
FROM --platform=linux/amd64 python:3.12.0-slim-bullseye
# Copy requirements.txt
COPY requirements.txt /tmp
# Install git CLI for running Mlflow from Git repositories and python packages
# Also install conda needed for mlflow environment
# https://repo.anaconda.com/archive/ OR https://repo.anaconda.com/miniconda/
RUN pip install -r /tmp/requirements.txt \
    && apt-get update \
    && apt-get install wget git  -y \
    && apt-get clean \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-py312_24.9.2-0-Linux-x86_64.sh -O ~/miniconda.sh \
    && bash ~/miniconda.sh -p /miniconda -b \
    && rm ~/miniconda.sh
ENV PATH=/miniconda/bin:${PATH}
# Resolve issue related to /lib/x86_64-linux-gnu/libstdc++.so.6: version 'GLIBCXX_3.4.29' not found
# Solution as per: https://github.com/pybind/pybind11/discussions/3453#discussioncomment-7068951
RUN conda install -y -c conda-forge libstdcxx-ng \
    && rm /usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
    && cp miniconda/lib/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/
