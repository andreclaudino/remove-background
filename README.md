# Remove Background

A command line tool to remove background form an image, or add a new background.

## Objective

When creating thumbnails for my youtube videos, I faced the need to take shots and extract only faces on foreground. Doing this with a lot of files take a long time which may be used in other tasks. Then I decided to automate the most I can using Python (then create the souce code used in a new video!)

To reach my objective, I created a command line job based on this jupyter notebook from [data-flair](https://data-flair.training/blogs/python-remove-image-background/). But instead of processing from webcam, I will process from a saved image on disk.


## How to use

This is a command line tool, there are the parameters:

```
remove-background --help
Usage: remove-background [OPTIONS]

Options:
  -s, --foreground-source-path TEXT
                                  The source path for the image containing the
                                  foreground face
  -b, --background-source-path TEXT
                                  The background image source path. If
                                  ignored, the resulting background will be
                                  transparent.
  -o, --output-path TEXT          The output path for each image
  -f, --output-format [png|webp|hdr|jpg|bmp]
                                  The output file format (file type) of the
                                  generated image
  --threshold FLOAT               Mask extraction threshold
  -h, --output-height INTEGER     The height of the output image. If ignored,
                                  will be calculated.
  -w, --output-width INTEGER      The width of the output image. If ignored,
                                  will be calculated.
  --keep-ratio BOOLEAN            Keep aspect ration on resize
  -r, --rotation INTEGER          Rotate image by this angle clockwise
  --face-xml-model TEXT           The path or URL to XML cascade model used to
                                  detect faces.
  --face-top-offset INTEGER       Top offset for face bounding box in px
  --face-bottom-offset INTEGER    Bottom offset for face bounding box in px
  --face-right-offset INTEGER     Right offset for face bounding box in px
  --face-left-offset INTEGER      Left offset for face bounding box in px
  --help                          Show this message and exi
```