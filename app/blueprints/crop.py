import os
from tempfile import gettempdir
from uuid import uuid4

from face_cropper import crop
from face_cropper.exceptions import NoFaceException, AboveThresholdException
from flask import Blueprint, request, send_file

crop_blueprint = Blueprint("crop", __name__)


@crop_blueprint.route("/crop_largest_face", methods=["POST"])
def crop_largest_face():
    if "image" not in request.files:
        return ("Missing image to crop", 400)

    face = request.files["image"]
    temp_location = gettempdir()
    temp_filename = uuid4()
    original_filename, extension = os.path.splitext(face.filename)
    temp_img_path = f"{temp_location}/{temp_filename}{extension}"
    face.save(temp_img_path)

    try:
        crop(
            image_path=temp_img_path,
            saving_path=temp_location
        )
    except (NoFaceException, AboveThresholdException) as exception:
        if isinstance(exception, NoFaceException):
            return ("No face has been found on the provided image", 422)
        else:
            return (
                "The face on the image is above the maximum size : 1024 * 1024",  # noqa: E501
                422
            )

    if "attachment" not in request.form or \
            request.form["attachment"].lower() == "false":
        response = send_file(
            f"{temp_location}/{temp_filename}_cropped{extension}",
            # Remove "." in file ext
            mimetype=f"image/{extension[1:]}",
        )
    else:
        response = send_file(
            f"{temp_location}/{temp_filename}_cropped{extension}",
            # Remove "." in file ext
            mimetype=f"image/{extension[1:]}",
            as_attachment=True,
            attachment_filename=f"{original_filename}_cropped{extension}"
        )
    return response
