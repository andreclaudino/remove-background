from typing import Tuple

import cv2
from numpy import ndarray


def resize_final_image(image: ndarray, output_width: int, output_height: int, keep_ratio: bool,
                       interpolation: int) -> ndarray:
    if output_width and output_height:

        if keep_ratio:
            output_width, output_height = _get_shape_to_keep_ratio(output_width, output_height, image)

        shape = (output_width, output_height)
        resized_output_image = cv2.resize(image, shape, interpolation=interpolation)
        return resized_output_image
    else:
        return image


def _get_shape_to_keep_ratio(output_width: int, output_height: int, image: ndarray) -> Tuple[int, int]:
    width, height, _ = image.shape
    ratio = width/height

    if width > height:
        output_height = int(width/ratio)
    else:
        output_width = int(ratio * height)

    return output_width, output_height
