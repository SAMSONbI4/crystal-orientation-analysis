# fft_analysis.py

import numpy as np
import cv2
from scipy.fft import fft2, fftshift


def compute_fft_histogram(masked_image: np.ndarray) -> np.ndarray:
    gray_masked = cv2.cvtColor(
        (masked_image * 255).astype(np.uint8),
        cv2.COLOR_RGB2GRAY
    )

    fft_result = fft2(gray_masked)
    fft_shifted = fftshift(fft_result)

    magnitude_spectrum = np.abs(fft_shifted)
    magnitude_spectrum = np.log1p(magnitude_spectrum)

    return magnitude_spectrum