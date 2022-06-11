import numpy as np
import cv2

import src.libs.ocr as ocr
import src.libs.encryptor as enc


class ColorNotFoundException(NotImplementedError):
    def __init__(self, message='Color type not found'):
        self.message = message
        super().__init__(self.message)


class ImageBase:
    path: str
    origin: np.ndarray
    data: np.ndarray
    data_type: str

    def __init__(self, path, flag=None):
        self.path = path
        self.origin = cv2.imread(path, flag or cv2.IMREAD_UNCHANGED)
        self.data = cv2.cvtColor(self.origin, cv2.COLOR_BGR2RGB)
        self.data_type = 'RGB'

    def get_origin(self):
        return self.origin

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_rgb(self):
        if self.data_type == 'RGB':
            return self.data
        elif self.data_type == 'GRAY':
            return cv2.cvtColor(self.data, cv2.COLOR_GRAY2RGB)
        elif self.data_type == 'BGR':
            return cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
        else:
            raise ColorNotFoundException()

    def get_bgr(self):
        if self.data_type == 'BGR':
            return self.data
        elif self.data_type == 'GRAY':
            return cv2.cvtColor(self.data, cv2.COLOR_GRAY2BGR)
        elif self.data_type == 'RGB':
            return cv2.cvtColor(self.data, cv2.COLOR_RGB2BGR)
        else:
            raise ColorNotFoundException()

    def get_grayscale(self):
        if self.data_type == 'GRAY':
            return self.data
        elif self.data_type == 'RGB':
            return cv2.cvtColor(self.data, cv2.COLOR_RGB2GRAY)
        elif self.data_type == 'BGR':
            return cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)
        else:
            raise ColorNotFoundException()

    def to_grayscale(self):
        if self.data_type == 'RGB':
            self.data = cv2.cvtColor(self.data, cv2.COLOR_RGB2GRAY)
        elif self.data_type == 'BGR':
            self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)
        elif self.data_type == 'GRAY':
            pass
        else:
            raise ColorNotFoundException()

        self.data_type = 'GRAY'
        return self.data


class SourceImage(ImageBase):
    def encrypt(self, secret) -> np.ndarray:
        self.data = enc.encrypt(self.data, secret)
        return self.data

    def decrypt(self, key) -> np.ndarray:
        self.data = enc.decrypt(self.data, key)
        return self.data


class TextImage(ImageBase):
    text: str

    def __init__(self, path, flag=None):
        super().__init__(path, flag)
        self.to_grayscale()

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def preprocess(self, *flags) -> None:
        self.data = ocr.preprocess(self.data, *flags)

    def postprocess(self, *flags) -> None:
        self.text = ocr.postprocess(self.text, *flags)

    def to_text(self, **flags) -> str:
        print("> OCR with flags:", flags)

        if flags and flags['preprocess']:
            self.preprocess(*flags['preprocess'])

        self.text = ocr.image_to_string(self.data)

        if 'postprocess' in flags:
            self.postprocess(*flags['postprocess'])

        return self.text
