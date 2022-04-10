from setuptools import setup

setup(
    name='remove-background',
    version='',
    packages=['remove_background'],
    url='',
    license='',
    author='André Claudino',
    author_email='',
    description='',
    install_requires=[
        "opencv-python==4.5.5.64",
        "mediapipe==0.8.9.1",
        "numpy==1.22.3",
        "smart-open[http]==5.2.1",
        "smart-open[s3]==5.2.1",
        "click==8.1.2"
    ],
    entry_points={
        'console_scripts': [
            "remove-background=remove_background.main:main"
        ]
    }
)
