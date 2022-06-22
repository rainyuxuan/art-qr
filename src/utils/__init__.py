import numpy as np
from PIL import Image
import cv2


def _split_filename(path):
    """Split a path to the directories and the file name.

    :param path:
    :return: dir, filename
    """
    entries = path.split("/")
    dir = ("/").join(entries[:-1])
    file = entries[-1]
    return dir, file


def convert_from_cv2_to_image(img: np.ndarray) -> Image:
    return Image.fromarray(img)


def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # return np.asarray(img)
