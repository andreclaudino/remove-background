from remove_background.persistence import load_image
from remove_background.processing.background import make_transparent_background


def load_or_create_background_image(background_source_path, foreground_image):
    if background_source_path:
        background_image = load_image(background_source_path, rotation=None, force_3_channels=False)
    else:
        background_image = make_transparent_background(foreground_image)
    return background_image
