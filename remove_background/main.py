import click
import cv2

from remove_background.entities.face_offset import FaceOffsets
from remove_background.persistence import load_image, save_image
from remove_background.persistence.background import load_or_create_background_image
from remove_background.processing import make_image_condition_mask
from remove_background.processing import merge_images
from remove_background.processing.face import crop_for_faces
from remove_background.processing.resize import resize_final_image


@click.command()
@click.option("--foreground-source-path", "-s", type=click.STRING,
              help="The source path for the image containing the foreground face")
@click.option("--background-source-path", "-b", type=click.STRING, default=None,
              help="The background image source path. If ignored, the resulting background will be transparent.")
@click.option("--output-path", "-o", type=click.STRING, help="The output path for each image")
@click.option("--output-format", "-f", type=click.Choice(choices=["png", "webp", "hdr", "jpg", "bmp"],
                                                         case_sensitive=False),
              default="png", help="The output file format (file type) of the generated image")
@click.option("--threshold", type=click.FLOAT, default=0.6, help="Mask extraction threshold")
@click.option("--output-height", "-h", type=click.INT, default=None,
              help="The height of the output image. If ignored, will be calculated.")
@click.option("--output-width", "-w", type=click.INT, default=None,
              help="The width of the output image. If ignored, will be calculated.")
@click.option("--keep-ratio", type=click.BOOL, default=True, help="Keep aspect ration on resize")
@click.option("--rotation", "-r", type=click.INT, default=0, help="Rotate image by this angle clockwise")
@click.option("--face-xml-model", type=click.STRING, default="https://bit.ly/3xawZsK",
              help="The path or URL to XML cascade model used to detect faces.")
@click.option("--face-top-offset", type=click.INT, default=200, help="Top offset for face bounding box in px")
@click.option("--face-bottom-offset", type=click.INT, default=400,
              help="Bottom offset for face bounding box in px")
@click.option("--face-right-offset", type=click.INT, default=50, help="Right offset for face bounding box in px")
@click.option("--face-left-offset", type=click.INT, default=50, help="Left offset for face bounding box in px")
def main(foreground_source_path: str, background_source_path: str, output_path: str, output_format: str,
         threshold: float, output_height: int, output_width: int, keep_ratio: bool, rotation: int, face_xml_model: str,
         face_top_offset: int, face_bottom_offset: int, face_left_offset: int, face_right_offset: int):

    foreground_image = load_image(foreground_source_path, rotation, force_3_channels=True)

    face_offset = FaceOffsets(face_top_offset, face_bottom_offset, face_left_offset, face_right_offset)
    image_cropped_for_faces = crop_for_faces(foreground_image, face_xml_model, face_offset)
    image_condition_mask = make_image_condition_mask(image_cropped_for_faces, threshold)

    background_image = load_or_create_background_image(background_source_path, foreground_image)

    combined_image = merge_images(image_cropped_for_faces, background_image, image_condition_mask)
    final_image = resize_final_image(combined_image, output_width, output_height, keep_ratio,
                                     interpolation=cv2.INTER_AREA)

    save_image(final_image, output_path, output_format)


if __name__ == '__main__':
    main()
