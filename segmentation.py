# segmentation.py

import numpy as np


def two_threshold_dither(image_gray: np.ndarray, low_thr: float, high_thr: float) -> np.ndarray:
    image_norm = np.clip(image_gray / 255.0, 0, 1)
    mask = np.logical_or(
        image_norm < (low_thr / 255.0),
        image_norm > (high_thr / 255.0)
    )
    return mask.astype(np.float32)


def apply_mask_to_original(original_rgb: np.ndarray, mask: np.ndarray) -> np.ndarray:
    masked = original_rgb.copy()
    mask_3ch = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    red_color = np.array([1.0, 0.0, 0.0], dtype=np.float32)
    masked = masked * mask_3ch + (1 - mask_3ch) * red_color
    return masked