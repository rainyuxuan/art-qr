from typing import Tuple

import numpy as np
import cv2
from matplotlib import pyplot as plt


class ImageIO:
    def __init__(self):
        self.plot_images = []

    def add_image_to_plot(self, name, image_data):
        self.plot_images.append((name, image_data))

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
