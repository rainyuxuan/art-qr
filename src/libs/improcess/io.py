from typing import Tuple

import numpy as np
import cv2
from matplotlib import pyplot as plt
from utils import *


class ImageIO:
    def __init__(self, need_convert=False):
        self.images = []
        self.need_convert = need_convert

    def add_image_to_plot(self, name: str, image_data: np.ndarray, need_convert=None):
        if need_convert is None:
            need_convert = self.need_convert
        self.images.append(
            (name, image_data if not need_convert else cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)))

    def remove_image(self, img_name: str):
        for i, (name, image) in enumerate(self.images):
            if name == img_name:
                self.images.pop(i)

    def plot(self):
        num_images = len(self.images)
        num_rows = num_images // 3 + (num_images % 3 != 0)

        idx = num_rows * 100 + 30

        for name, image_data in self.images:
            idx += 1
            plt.subplot(idx)
            plt.imshow(image_data)
            plt.title(name)

        plt.show()

    def show(self, img_name: str = None):
        if img_name is not None:
            for name, image in self.images:
                if name == img_name:
                    convert_from_cv2_to_image(image).show()
        else:
            for name, image in self.images:
                convert_from_cv2_to_image(image).show()

    def save_images(self, directory: str = './out', file_format: str = 'jpg'):
        for name, image in self.images:
            # print(name, image)
            cv2.imwrite(f"{directory}/{name}.{file_format}", image)
