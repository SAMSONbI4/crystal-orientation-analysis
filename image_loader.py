# image_loader.py

import cv2
import numpy as np


def load_and_preprocess(image_path: str, sigma: float):
    original_bgr = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if original_bgr is None:
        raise FileNotFoundError(f"Failed to open image file: {image_path}")

    original_rgb = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    gray = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)

    kernel_size = int(6 * sigma + 1)
    if kernel_size % 2 == 0:
        kernel_size += 1

    blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), sigma).astype(np.float32)

    return original_rgb, blurred