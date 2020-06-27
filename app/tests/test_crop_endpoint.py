from .utils import mock_file


def test_crop_endpoint_returns_400_when_no_file_is_provided(client):
    response = client.post("/crop_largest_face")
    assert response.status_code == 400
    assert "Missing image to crop" in response.data.decode("utf-8")


def test_crop_endpoint_returns_200_when_file_is_provided(client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("child.jpeg")},
        content_type='multipart/form-data'
    )
    assert response.status_code == 200


def test_crop_endpoint_returns_attachement_if_param_is_provided(client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("child.jpeg"), "attachment": "true"},
        content_type='multipart/form-data'
    )
    assert response.status_code == 200
    assert "attachment" in response.headers["Content-Disposition"]
    assert "filename=child_cropped.jpeg" in response.headers["Content-Disposition"]  # noqa: E501


def test_crop_endpoint_doesnt_return_attachement_param_is_absent_or_false(
        client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("child.jpeg"), "attachment": "false"},
        content_type='multipart/form-data'
    )
    assert response.status_code == 200
    assert "Content-Disposition" not in response.headers


def test_crop_endpoint_returns_422_when_no_face_is_found(client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("no_face.jpeg")},
        content_type='multipart/form-data'
    )
    assert response.status_code == 422
    assert "No face has been found on the provided image" in \
        response.data.decode("utf-8")


def test_crop_endpoint_returns_422_when_face_is_above_threshold(client):
    response = client.post(
        "/crop_largest_face",
        data={"image": mock_file("above_threshold.jpg")},
        content_type='multipart/form-data'
    )
    assert response.status_code == 422
    assert "The face on the image is above the maximum size : 1024 * 1024" in \
        response.data.decode("utf-8")
