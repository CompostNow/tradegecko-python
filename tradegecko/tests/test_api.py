from mock import patch, Mock

import pytest

from tradegecko import errors
from tradegecko.api import ApiEndpoint


NAME = "object"
NAME_LIST = "objects"


@pytest.fixture()
def api():
    return ApiEndpoint(
        url="foo/%s", auth_token="auth_token", name=NAME, name_list=NAME_LIST
    )


def _validate_post_data(endpoint, data):
    for k in endpoint.required_fields:
        if k not in data.keys():
            return False
    return True


def test_validate_post_data_correct_fields(api):
    api.required_fields = ["field1", "field2"]
    data = {"field1": "foo", "field2": "bar"}

    assert _validate_post_data(api, data)


def test_validate_post_data_incorrect_fields(api):
    api.required_fields = ["field1", "field3"]
    data = {"field1": "foo", "field2": "bar"}

    assert not _validate_post_data(api, data)


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=200))
def test_send_request(request, api):
    assert api._request("GET", "uri") == 200  # returns status code
    assert request.called  # request is called


# All
@patch(
    "tradegecko.api.requests.request",
    return_value=Mock(
        status_code=200, json=Mock(return_value={NAME_LIST: [{"foo": "bar"}]})
    ),
)
def test_all_request_success(_, api):
    assert api.all() == [{"foo": "bar"}]  # dict on request success


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=400))
def test_all_request_failure(_, api):
    with pytest.raises(errors.ListObjectsError):
        api.all()


# Retrieve
@patch(
    "tradegecko.api.requests.request",
    return_value=Mock(
        status_code=200, json=Mock(return_value={NAME: {"foo": "bar"}})
    ),
)
def test_get_request_success(_, api):
    assert api.get(123) == {"foo": "bar"}  # dict on request success


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=400))
def test_get_request_failure(_, api):
    with pytest.raises(errors.GetObjectError):
        api.get(123)


# create
@patch(
    "tradegecko.api.requests.request",
    return_value=Mock(
        status_code=201, json=Mock(return_value={NAME: {"id": 1}})
    ),
)
def test_create_request_success(_, api):
    assert api.create({"foo": "bar"})["id"] == 1


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=400))
def test_create_request_fail(_, api):
    data = {"foo": "bar"}
    with pytest.raises(errors.CreateObjectError):
        api.create(data)


# update
@patch("tradegecko.api.requests.request", return_value=Mock(status_code=204))
def test_update_request_success(_, api):
    assert api.update(1234, {"foo": "bar"})


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=400))
def test_update_request_fail(_, api):
    with pytest.raises(errors.UpdateObjectError):
        api.update(1234, {"foo": "bar"})


# Delete
@patch("tradegecko.api.requests.request", return_value=Mock(status_code=204))
def test_delete_request_success(_, api):
    assert api.delete(123)


@patch("tradegecko.api.requests.request", return_value=Mock(status_code=400))
def test_delete_request_failure(_, api):
    with pytest.raises(errors.DeleteObjectError):
        api.delete(123)
