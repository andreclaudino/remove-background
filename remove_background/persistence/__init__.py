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

    original_height, original_width, _ = image.shape

    rotation_cos = np.abs(rotation_operator[0, 0])
    rotation_sin = np.abs(rotation_operator[0, 1])

    transformed_width = int((original_height * rotation_sin) + (original_width * rotation_cos))
    transformed_height = int((original_height * rotation_cos) + (original_width * rotation_sin))

    rotation_operator[0, 2] += (transformed_width / 2) - original_width//2
    rotation_operator[1, 2] += (transformed_height / 2) - original_height//2

    rotated_image = cv2.warpAffine(image, rotation_operator, (transformed_width, transformed_height),
                                   flags=cv2.INTER_CUBIC)
    return rotated_image
