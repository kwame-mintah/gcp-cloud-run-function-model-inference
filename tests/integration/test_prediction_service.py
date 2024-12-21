import os

import requests
from pytest_bdd import scenario, given, parsers, then
from pytest_bdd.gherkin_parser import DataTable

result = {}
payload = {}
integration_tests_base_url = os.getenv(
    "INTEGRATION_TESTS_BASE_URL", default="http://localhost:8080"
)


@scenario(
    feature_name="test_prediction_service.feature",
    scenario_name="A user should be able to make a prediction",
)
def test_prediction_service(setup):
    """
    Cucumber scenario
    """


@given(name=parsers.parse("a user has wine quantitative features for prediction"))
def parse_wine_quantitative_features_for_prediction(datatable: DataTable):
    """
    Parse the `DataTable` from the Gherkin file into a dict object ready to
    be used as a payload.
    :param datatable: [DataTable](https://pytest-bdd.readthedocs.io/en/8.1.0/#datatables)
    """
    data = {}

    for heading, value in list(zip(datatable[:1][0], datatable[1:][0])):
        data[heading] = value

    payload["data"] = [data]


@then(name=parsers.parse("they make a prediction against {url}"))
def make_prediction_request_to_url(url: str):
    """
    Use payload to send a POST request to the provided endpoint
    :param url: url path
    """
    response = requests.post(url=integration_tests_base_url + url, json=payload["data"])
    result["response"] = response


@then(name=parsers.parse("the response status code should be {status}"))
def response_status_code_should_be(status: str):
    """
    Check the HTTP status code is the expected value
    :param status: HTTP response status code
    """
    assert result["response"].status_code == int(status)
