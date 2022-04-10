from mediapipe.python.solutions.selfie_segmentation import SelfieSegmentation
from numpy import ndarray, stack


def make_image_condition_mask(image: ndarray, threshold: float) -> ndarray:
    segmentation_mask = _get_segmentation_mask(image)
    condition_mask = _create_condition_mask(segmentation_mask, threshold)
    return condition_mask


def _create_condition_mask(segmentation_mask, threshold) -> ndarray:
    condition_mask = stack((segmentation_mask,) * 3, axis=-1) > threshold
    return condition_mask


def _get_segmentation_mask(image) -> ndarray:
    segmentation_model_code = _get_sementation_model_code(image)
    selfie_segmentator = SelfieSegmentation(model_selection=segmentation_model_code)
    segmentation_result = selfie_segmentator.process(image)
    mask = segmentation_result.segmentation_mask
    return mask


def _get_sementation_model_code(image: ndarray) -> int:
    """
    If image is portrait or square, use REGULAR (0), else use OPTIMIZED for landscape (1)
    :param image (ndarray): The source image
    :return: the segmentation model code (int)
    """
    width, height, _ = image.shape

    if height >= width:
        segmentation_model_code = 0
    else:
        segmentation_model_code = 1

    return segmentation_model_code
