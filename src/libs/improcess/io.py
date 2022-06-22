from typing import Tuple

import numpy as np
import cv2
from matplotlib import pyplot as plt


class ImageIO:
    def __init__(self, need_convert=False):
        self.plot_images = []
        self.need_convert = need_convert

    def add_image_to_plot(self, name, image_data, need_convert=None):
        if need_convert is None:
            need_convert = self.need_convert
        self.plot_images.append(
            (name, image_data if not need_convert else cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)))

    def plot(self):
        num_images = len(self.plot_images)
        num_rows = num_images // 3 + (num_images % 3 != 0)

        idx = num_rows * 100 + 30

        for name, image_data in self.plot_images:
            idx += 1
            plt.subplot(idx)
            plt.imshow(image_data)
            plt.title(name)

        plt.show()
