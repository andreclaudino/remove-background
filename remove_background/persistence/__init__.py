from typing import Optional

import numpy as np
from numpy import ndarray
from smart_open import open
import cv2


def load_image(image_path: str, rotation: Optional[int], force_3_channels: bool) -> ndarray:
    image_buffer = _load_image_buffer(image_path)
    image = cv2.imdecode(image_buffer, -1)

    if force_3_channels:
        _, _, channels = image.shape
        if channels == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

    if rotation:
        rotated_image = _rotate_image(image, rotation)
        return rotated_image
    else:
        return image


def _load_image_buffer(image_path: str) -> ndarray:
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_np_array = np.frombuffer(image_bytes, np.uint8)
    return image_np_array


def save_image(image, output_path: str, output_format: str):
    output_format = f".{output_format}"
    ok, image_file_data = cv2.imencode(output_format, image)

    if ok:
        with open(output_path, "wb") as output_file:
            output_file.write(image_file_data)
    else:
        raise ValueError("Invalid file format for output")


def _rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rotation_operator = cv2.getRotationMatrix2D(image_center, -angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_operator, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return rotated_image
