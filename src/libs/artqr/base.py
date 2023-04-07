import cv2
import numpy as np


class QRCodeImage:
    path: str
    image: np.ndarray
    data: str
    variants: [np.ndarray]

    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    def data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def display(self, bbox):
        n = len(bbox)
        for j in range(n):
            cv2.line(self.image, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)
        cv2.imshow("Results", self.image)

    def decode_image(self):
        """
        Decode the QR code in the image
        :return: data, bbox, rectified
        """
        code_detector = cv2.QRCodeDetector()
        data, bbox, rectified = code_detector.detectAndDecode(self.image)
        if len(data) > 0:
            print(f"Decoded Data : {data}")
            # self.display(bbox)
            rectified = np.uint8(rectified)
        else:
            raise "QR Code not detected"

        self.data = data
        return data, bbox, rectified


class ArtQRCodeConfig:
    def set(self, **kwargs):
        for kw, value in kwargs:
            self.__setattr__(kw, value)


class ArtQRCode:
    def __init__(self, data: str, config: ArtQRCodeConfig):
        self.data = data
        self.config = config

    def set_config(self, config: ArtQRCodeConfig):
        self.config = config

    def update_config(self, **kwargs):
        for kw, value in kwargs:
            self.config.__setattr__(kw, value)

    def make(self):
        pass

