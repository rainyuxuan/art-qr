import pytesseract
from pytesseract import Output
import argparse
import numpy as np
import cv2
import os

BLUR_MEDIAN = 3


def preprocess(image_data: np.ndarray, *flags):
    print('> Preprocess with flags', flags)
    processed_image = image_data
    if 'threshold' in flags:
        processed_image = cv2.threshold(image_data, 0, 255,
                                        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if 'blur' in flags:
        processed_image = cv2.medianBlur(processed_image, BLUR_MEDIAN)

    return processed_image


def postprocess(text: str, *flags):
    print('> Postprocess with flags', flags)
    processed_text = text

    return processed_text


def image_to_string(image_data: np.ndarray):
    return pytesseract.image_to_string(image_data)


def show_boxes(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)

    # Reference: https://nanonets.com/blog/ocr-with-tesseract/
    n_boxes = len(d['text'])
    boxed_image = image
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            boxed_image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow('Boxed img', boxed_image)
    # cv2.waitKey(0)
    return boxed_image