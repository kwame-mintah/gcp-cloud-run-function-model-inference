from time import sleep

import pytest
from testcontainers.compose import DockerCompose

docker_compose = DockerCompose(
    context="docker",
    build=True,
    services=["fastapi"],
)


@pytest.fixture(scope="session")
def setup(request):
    """Start the docker container service(s)"""
    docker_compose.start()
    # Due to the choice of the docker base image (python:3.12.0-slim-bullseye) being used,
    # unable to use `curl` as a healthcheck, so have to use a temp sleep.
    sleep(10)

    def remove_container():
        """Stop the docker container(s)"""
        docker_compose.stop()

    request.addfinalizer(remove_container)
