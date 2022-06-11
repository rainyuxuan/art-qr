import pytesseract
import argparse
import numpy as np
import cv2
import os


def preprocess(image_data: np.ndarray, *flags):
    print('> Preprocess with flags', flags)
    processed_image = image_data
    if 'threshold' in flags:
        processed_image = cv2.threshold(image_data, 0, 255,
                                        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if 'blur' in flags:
        processed_image = cv2.medianBlur(processed_image, 3)

    return processed_image


def postprocess(text: str, *flags):
    print('> Postprocess with flags', flags)
    processed_text = text

    return processed_text


def image_to_string(image_data: np.ndarray):
    return pytesseract.image_to_string(image_data)

