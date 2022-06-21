"""
Code Reference: https://github.com/chinuno-usami/CuteR
"""

import PIL
from PIL import Image
import numpy as np
import qrcode

from .base import ArtQRCode

DEFAULT_CONFIG = {
    'version': 5,
    'error_correction': qrcode.constants.ERROR_CORRECT_H,
    'brightness': 1.0,
    'contrast': 1.0,
    'bg': (255, 255, 255, 1),
    'pixelate': False,
    'mask_crop_pos': (0, 0),
    'resize': 1.0
}

SQUARE_SIZE_LARGE = 7  # number of pixels of the length of a locator square
SQUARE_SIZE_SMALL = 5  # number of pixels of the length of a locator square


class CuteRCodeConfig:
    version = 3
    error_correction = qrcode.constants.ERROR_CORRECT_H
    brightness = 1.0
    contrast = 1.0
    bg_rgb = (255, 255, 255)
    pixelate = False
    mask_crop_pos = (0, 0)
    resize = 1.0

    def __init__(self,
                 version=3,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 brightness=1.0,
                 contrast=1.0,
                 bg_rgb=(255, 255, 255),
                 pixelate=False,
                 mask_crop_pos=(0, 0),
                 resize=1.0):
        self.version = version
        self.error_correction = error_correction
        self.brightness = brightness
        self.contrast = contrast
        self.bg_rgb = bg_rgb
        self.pixelate = pixelate
        self.mask_crop_pos = mask_crop_pos
        self.resize = resize

    def set(self, name, value):
        self.__setattr__(name, value)


class CuteRCode(ArtQRCode):
    def __init__(self, data: str, mask_path: str, config: CuteRCodeConfig = CuteRCodeConfig()):
        super().__init__(data, config)
        self.mask = Image.open(mask_path)

    def make(self):
        # Make base QR Code
        qr = qrcode.QRCode(version=self.config.version,
                           error_correction=self.config.error_correction,
                           box_size=1,
                           border=0)
        qr.add_data(self.data)
        qr.make(fit=True)

        qr_make = qr.make_image(fill_color=self.config.bg_rgb)
        original_size = qr_make.pixel_size  # original qr-code image size

        # Get a resized, cropped mask image and the result_image size
        mask_img = self.mask.convert('RGBA')
        mask_img = mask_img.resize((mask_img.size[0] * self.config.resize,
                                    mask_img.size[1] * self.config.resize),
                                   PIL.Image.NEAREST)
        img_size = min(mask_img.size[0], mask_img.size[1])
        img_size = img_size - (img_size % original_size)    # Guarantees an integer factor
        mask_img = mask_img.crop(self.config.mask_crop_pos + (img_size, img_size))

        scale = img_size // original_size   # == size of a qr-code pixel

        # Image of the base QR code in RGBA format
        qr_img = qr.make_image().convert('RGBA')
        qr_img = qr_img.resize((img_size, img_size), PIL.Image.NEAREST)

        # Enhance Contrast and Brightness

        qr_img_grayscale = qr_img.convert('L')

        corner_size = int(SQUARE_SIZE_LARGE * scale)

        for x in range(0, int(scale)):
            for y in range(0, int(scale)):
                qr_img.putpixel((corner_size + x, corner_size + y), (200, 18, 18, 255))

        # Produce each pixel
        # for x in range(0, img_size):
        #     for y in range(0, img_size):
        #         if corner_size < x and
        #             pass
                # Skip locators
                #
                # if x < 24 and (y < 24 or y > img_size - 25):
                #     continue
                # if x > img_size - 25 and (y < 24):
                #     continue
                # if (x % 3 == 1 and y % 3 == 1):
                #     if (qr_img_grayscale.getpixel((x + 12, y + 12)) > 70 and qr_img_grayscale.getpixel((x, y)) < 185) \
                #             or (qr_img_grayscale.getpixel((x + 12, y + 12)) < 185 and qr_img_grayscale.getpixel((x, y)) > 70):
                #         continue
                # qr_img.putpixel((x, y), (0, 0, 0, 0))

        qr_img.show()
        pass
        # pos = qrcode.util.pattern_position(qr.version)
        # img_qr2 = qr.make_image().convert("RGBA")
        # for i in pos:
        #     for j in pos:
        #         if (i == 6 and j == pos[-1]) or (j == 6 and i == pos[-1]) \
        #                 or (i == 6 and j == 6):
        #             continue
        #         else:
        #             rect = (3 * (i - 2) + 12, 3 * (j - 2) + 12, 3 * (i + 3) + 12, 3 * (j + 3) + 12)
        #             img_tmp = img_qr2.crop(rect)
        #             qr_img.paste(img_tmp, rect)
        #
        # img_res = Image.new("RGBA", (qr_img.size[0] * 10, qr_img.size[1] * 10), (255, 255, 255, 255))
        # img_res.paste(mask_img, (120, 120), mask_img)
        # img_frame = qr_img.resize((qr_img.size[0] * 10, qr_img.size[1] * 10), Image.NEAREST)
        # img_res.paste(img_frame, (0, 0), img_frame)
        # img_res = img_res.convert('RGB')
        #
        # img_res.show()
        # return result
