import cv2
from numpy import ndarray, where
import numpy as np


def merge_images(foreground_image: ndarray, background_image: ndarray, image_condition_mask: ndarray) -> ndarray:
    output_image = _merge_back_and_front(background_image, foreground_image, image_condition_mask)

    return output_image


def _merge_back_and_front(background_image, foreground_image, image_condition_mask):
    foreground_height, foreground_width, foreground_channels = foreground_image.shape
    _, _, background_channels = background_image.shape

    if background_channels == 4 and foreground_channels == 3:
        foreground_image = cv2.cvtColor(foreground_image, cv2.COLOR_RGB2RGBA)
        image_condition_mask = np.array(image_condition_mask, dtype=np.uint8)
        image_condition_mask = cv2.cvtColor(image_condition_mask, cv2.COLOR_RGB2RGBA)
        image_condition_mask = image_condition_mask != 0

    resized_background = cv2.resize(background_image, (foreground_width, foreground_height))
    output_image = where(image_condition_mask, foreground_image, resized_background)
    return output_image
