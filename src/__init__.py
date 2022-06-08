import random

import cv2
import numpy as np
from matplotlib import pyplot as plt

from libs.improcess import *
from libs.improcess.io import ImageIO
import libs.ocr as ocr


def test_procedures(source_path="assets/test_images/target-1.jpg", key_path="assets/test_images/text-2.jpg"):
    print(f"######## Start testing {source_path} ########")
    imio = ImageIO()

    ######## ENCRYPT IMAGE ########
    # Read original image
    source_image = SourceImage(source_path)

    imio.add_image_to_plot("source_image", source_image.data)

    # Get text_secret
    text_secret = "Every path is the right path."

    # Encrypt original_img with text_secret
    encrypted_img_data = source_image.encrypt(text_secret)

    # Output encrypted_img
    encrypted_img_path = source_path + '.encrypted.jpg'
    cv2.imwrite(encrypted_img_path, cv2.cvtColor(encrypted_img_data, cv2.COLOR_RGB2BGR))

    encrypted_image = SourceImage(encrypted_img_path)
    imio.add_image_to_plot("encryted_image", encrypted_image.data)

    ######## DECRYPT IMAGE ########
    # Get password_image
    password_img = TextImage(key_path)

    imio.add_image_to_plot("password_img", cv2.cvtColor(password_img.data, cv2.COLOR_GRAY2RGB))

    # Extract password
    text_key = password_img.to_text()
    print(text_key)

    # Decrypt encrypted_img with text_key
    decrypted_img_data = encrypted_image.decrypt(text_key)

    # Output decrypted_img with text_key
    decrypted_img_path = source_path + '.decrypted.jpg'
    cv2.imwrite(decrypted_img_path, cv2.cvtColor(decrypted_img_data, cv2.COLOR_RGB2BGR), )

    decrypted_image = SourceImage(decrypted_img_path)
    imio.add_image_to_plot("decrypted_image", decrypted_image.data)

    imio.plot()


def test_ocr(image_path="assets/test_images/text-1.jpg"):
    image = TextImage(image_path)
    recognized_text = image.to_text()
    print(f"Recognized path for {image_path}:", recognized_text)


if __name__ == '__main__':
    print("Hello world")
    test_procedures()
