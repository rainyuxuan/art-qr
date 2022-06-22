import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image

from src.libs.improcess.io import ImageIO
from src.utils import *
from src.libs.artqr.base import *
from src.libs.artqr.CuteR import CuteRCode, CuteRCodeConfig


def test_CuteR(data="Data placeholder", bg_image_path='../assets/test_images/qr-bg-marisa.jpg'):
    config = CuteRCodeConfig(box_factor=3, transparency=0.75, contrast=0.8, bg_rgb=(100, 50, 100))
    cuter = CuteRCode(data, bg_image_path, config)
    result_img, qr_img = cuter.make()
    return convert_from_image_to_cv2(result_img), convert_from_image_to_cv2(qr_img)


def main(input_path='../assets/test_images/secrets/qr-wechat.jpg'):
    # Initialize plot
    imio = ImageIO(need_convert=True)

    # Read in an image with QR Code
    input_image = QRCodeImage(input_path)
    imio.add_image_to_plot('input', input_image.image)

    # Decode to get original data
    data, bbox, rectified = input_image.decode_image()
    # imio.add_image_to_plot('bbox', bbox)
    imio.add_image_to_plot('rectified', rectified)

    # CuteR image
    cuter_img, cuter_qr_img = test_CuteR(data=data)
    imio.add_image_to_plot('CuteR', cuter_img, need_convert=True)
    imio.add_image_to_plot('CuteR QR', cuter_qr_img, need_convert=True)

    imio.plot()


if __name__ == '__main__':
    main()
