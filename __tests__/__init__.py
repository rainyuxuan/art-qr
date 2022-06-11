import random

import cv2
import numpy as np
from matplotlib import pyplot as plt

from src.libs.improcess import *
from src.libs.improcess.io import ImageIO


def _split_filename(path):
    entries = path.split("/")
    dir = ("/").join(entries[:-1])
    file = entries[-1]
    return dir, file

def test_procedures(source_path="../assets/test_images/target-1.jpg", key_path="../assets/test_images/text-4.jpg"):
    print(f"######## Start testing {source_path} ########")
    imio = ImageIO()

    # Extract filenames
    source_dir, source_file = _split_filename(source_path)
    key_dir, key_file = _split_filename(key_path)

    ######## ENCRYPT IMAGE ########
    # Read original image
    source_image = SourceImage(source_path)

    imio.add_image_to_plot("source_image", source_image.data)

    # Get text_secret
    text_secret = "Every path is the right path."

    # Encrypt original_img with text_secret
    encrypted_img_data = source_image.encrypt(text_secret)

    # Output encrypted_img
    encrypted_img_path = source_dir + "/out/" + source_file + '.encrypted.jpg'
    cv2.imwrite(encrypted_img_path, cv2.cvtColor(encrypted_img_data, cv2.COLOR_RGB2BGR))

    encrypted_image = SourceImage(encrypted_img_path)
    imio.add_image_to_plot("encryted_image", encrypted_image.data)

    ######## DECRYPT IMAGE ########
    # Get password_image
    password_img = TextImage(key_path)

    imio.add_image_to_plot("password_img", password_img.get_rgb())

    # Extract password
    # Preprocessing
    preprocess_flags = ['blur', 'threshold']
    password_img.preprocess(*preprocess_flags)
    imio.add_image_to_plot('preprocessed', password_img.get_rgb())

    # Output preprocessed image
    preprocessed_img_path = key_dir + "/out/" + key_file + \
                            f'.preprocessed.{preprocess_flags}.jpg'
    cv2.imwrite(preprocessed_img_path, password_img.get_rgb())

    # Recognize text
    text_key = password_img.to_text()
    print('#' * 20 + '\n' + text_key + '\n' + '#' * 20)

    # Decrypt encrypted_img with text_key
    decrypted_img_data = encrypted_image.decrypt(text_key)

    # Output decrypted_img with text_key
    decrypted_img_path = source_dir + "/out/" + source_file + '.decrypted.jpg'
    cv2.imwrite(decrypted_img_path, cv2.cvtColor(decrypted_img_data, cv2.COLOR_RGB2BGR))

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
