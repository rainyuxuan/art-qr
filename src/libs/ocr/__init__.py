import pytesseract
import argparse
import numpy as np
import cv2
import os


def preprocess(image_data: np.ndarray, *flags):
    return image_data


def postprocess(text: str):
    pass


def image_to_string(image_data: np.ndarray):
    return pytesseract.image_to_string(image_data)

