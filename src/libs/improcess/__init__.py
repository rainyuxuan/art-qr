import numpy as np
import cv2

import src.libs.ocr as ocr
import src.libs.encryptor as enc


class ImageBase:
    path: str
    origin: np.ndarray
    data: np.ndarray
    data_type: str

    def __init__(self, path, flag=None):
        self.path = path
        self.origin = cv2.imread(path, flag or cv2.IMREAD_UNCHANGED)
        self.data = cv2.cvtColor(self.origin, cv2.COLOR_BGR2RGB)
        self.data_type = 'rgb'

    def get_origin(self):
        return self.origin

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_rgb(self):
        return self.origin

    def to_grayscale(self):
        self.data = cv2.cvtColor(self.data, cv2.COLOR_RGB2GRAY)
        return self.data


class SourceImage(ImageBase):
    def encrypt(self, secret) -> np.ndarray:
        return enc.encrypt(self.data, secret)

    def decrypt(self, key) -> np.ndarray:
        return enc.decrypt(self.data, key)


class TextImage(ImageBase):
    text: str

    def __init__(self, path, flag=None):
        super().__init__(path, flag)
        self.to_grayscale()

    def set_text(self, text):
        self.text = text

    def preprocess(self, *flags) -> None:
        self.data = ocr.preprocess(self.data, flags)

    def to_text(self, *flags) -> str:
        self.preprocess(flags)
        return ocr.image_to_string(self.data)

