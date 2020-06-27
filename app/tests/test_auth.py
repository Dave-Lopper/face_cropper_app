import os

from .utils import mock_file


def test_no_api_key_returns_401_and_excepted_message(client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("child.jpeg")},
    )
    assert response.status_code == 401
    assert "No API key provided" in response.data.decode("utf-8")


def test_bad_api_key_returns_401_and_excepted_message(client):
    response = client.post(
        "/crop_largest_face",
        headers={"x-api-key": "bad_key"},
        data={"image": mock_file("child.jpeg")},
    )
    assert response.status_code == 401
    assert "Bad API key provided" in response.data.decode("utf-8")


def test_right_api_key_returns_200(client):
    response = client.post(
        "/crop_largest_face",
        headers={"x-api-key": os.environ["API_KEY"]},
        data={"image": mock_file("child.jpeg")},
    )
    assert response.status_code == 200
