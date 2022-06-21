import random

import cv2
import numpy as np
from matplotlib import pyplot as plt

from src.libs.improcess.io import ImageIO
from src.utils import *
from src.libs.artqr.base import *
from src.libs.artqr.CuteR import CuteRCode


def test_CuteR(data="this is the data", mask_image_path='../assets/test_images/qr-mask.jpg'):
    cuter = CuteRCode(data, mask_image_path)
    cuter.make()


def main(input_path='../assets/test_images/qr-2.jpg'):
    imio = ImageIO(need_convert=True)

    input_image = QRCodeImage(input_path)

    imio.add_image_to_plot('input', input_image.image)

    data, bbox, rectified = input_image.decode_image()
    # imio.add_image_to_plot('bbox', bbox)
    imio.add_image_to_plot('rectified', rectified)

    imio.plot()





if __name__ == '__main__':
    test_CuteR()
