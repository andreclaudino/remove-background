import os.path
from typing import Tuple, List

import cv2
from numpy import ndarray
from smart_open import open

from functools import reduce

from remove_background.entities.face_offset import FaceOffsets

BoundingBox = Tuple[int, int, int, int]


def crop_for_faces(image: ndarray, face_cascade_model_path: str, face_offsets: FaceOffsets) -> ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = _load_face_cascade(face_cascade_model_path)
    final_bounding_box = _make_bounding_box(face_cascade, gray_image)

    cropped_image = face_offsets.crop(image, final_bounding_box)

    return cropped_image


def _make_bounding_box(face_cascade, gray_image):
    boundind_boxes: List[BoundingBox] = face_cascade.detectMultiScale(gray_image, 1.1, 4, flags=cv2.CASCADE_SCALE_IMAGE)
    final_bounding_box = reduce(merge_bounding_box, boundind_boxes)
    return final_bounding_box


def _load_face_cascade(face_cascade_model_path):
    local_cascade_file_path = _get_local_model_path(face_cascade_model_path)
    face_cascade = cv2.CascadeClassifier(local_cascade_file_path)
    return face_cascade


def _get_local_model_path(face_cascade_model_path: str) -> str:
    if os.path.isfile(face_cascade_model_path):
        return face_cascade_model_path

    local_path = "face_model.xml"

    with open(face_cascade_model_path) as source:
        with open(local_path, 'w') as output:
            data = source.read()
            output.writelines(data)

    return local_path


def merge_bounding_box(bounding_box1: BoundingBox, bounding_box2: BoundingBox) -> BoundingBox:
    """
    TODO: Need correction for detecting more than one face
    :param bounding_box1:
    :param bounding_box2:
    :return:
    """
    x = min(bounding_box1[0], bounding_box2[0])
    y = min(bounding_box1[1], bounding_box2[1])

    width = max(bounding_box1[2], bounding_box2[2])
    height = max(bounding_box1[3], bounding_box2[3])

    return x, y, width, height
