import os
from pathlib import Path

from werkzeug.datastructures import FileStorage


def mock_file(filename: str):
    image_path = os.path.join(
        Path(__file__).parent.absolute(),
        f"samples/{filename}"
    )
    extension = os.path.splitext(filename)[1]
    mocked_file = FileStorage(
        stream=open(image_path, "rb"),
        filename="child.jpeg",
        content_type=f"image/{extension}",
    )
    return mocked_file
