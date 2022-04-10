import numpy as np
from numpy import ndarray


def make_transparent_background(foreground_image: ndarray) -> ndarray:
    foreground_height, foreground_width, _ = foreground_image.shape
    channels = 4
    transparent_image = np.zeros((foreground_height, foreground_width, channels), dtype=np.uint8)

    return transparent_image
