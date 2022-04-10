from typing import Tuple

from numpy import ndarray


class FaceOffsets:
    def __init__(self, face_top_offset: int, face_bottom_offset: int,
                 face_left_offset: int, face_right_offset: int):

        self._face_top_offset = face_top_offset
        self._face_bottom_offset = face_bottom_offset
        self._face_left_offset = face_left_offset
        self._face_right_offset = face_right_offset

    @property
    def top(self):
        return self._face_top_offset

    @property
    def bottom(self):
        return self._face_bottom_offset

    @property
    def left(self):
        return self._face_left_offset

    @property
    def right(self):
        return self._face_right_offset

    def crop(self, image: ndarray, bounding_box: Tuple[int, int, int, int]):
        (x, y, width, height) = bounding_box

        max_width, max_height, _ = image.shape

        start_x = max(x - self.left, 0)
        end_x = min(x + width + self.right, max_width)

        start_y = max(y - self.top, 0)
        end_y = y + height + self.bottom

        cropped = image[start_y:end_y, start_x:end_x]

        return cropped
